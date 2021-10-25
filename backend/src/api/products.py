from flask import jsonify
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist, authentification_required

from database.database import Database
from database.user import User
from database.product import Product, UserProductAssociation

ns = Namespace('products', description='Selling products')

USER_PRODUCTS_UPDATE_PARAMS = ns.model('Updating user products parameter', {
    "product_id": fields.Integer(required=True),
    "adding": fields.Boolean(required=True),
})


@ns.route('/products')
class Products(Resource):
    @authentification_required
    def get(self):
        products = []
        with Database(auto_commit=True) as db:
            for p in db.query(Product).all():
                products.append(p.to_dict())
        return jsonify(products)


@ns.route('/products/user/<card_uid>')
class UserProducts(Resource):
    @authentification_required
    @ns.expect(USER_PRODUCTS_UPDATE_PARAMS, validate=True)
    def put(self, card_uid):
        product_id = int(ns.payload["product_id"])
        adding = bool(ns.payload["adding"])

        abort_if_doesnt_exist(
            product_id,
            adding,
            message="Server could not get parameters properly",
            code=500
        )

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            abort_if_doesnt_exist(user, code=400, message="No user found with this card id")

            product = db.query(Product).filter_by(product_id=product_id).first()
            abort_if_doesnt_exist(product, code=400, message="No product found with this product id")

            if adding:
                product_association = db.query(UserProductAssociation).filter_by(
                    user_id=user.user_id).filter_by(product_id=product_id).first()
                if not product_association:
                    product_association = UserProductAssociation(
                        product_id=product_id,
                        user_id=user.user_id,
                        count=1,
                        product=product
                    )
                else:
                    product_association.count += 1
                user.products.append(product_association)
            else:
                product_association = db.query(UserProductAssociation).filter_by(
                    user_id=user.user_id).filter_by(product_id=product_id).first()
                if product_association.count > 0:
                    product_association.count -= 1
                user.products.append(product_association)
            db.commit()

        return True

    @authentification_required
    def delete(self, card_uid):
        abort_if_doesnt_exist(
            message="Server could not get parameters properly",
            code=500
        )

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            abort_if_doesnt_exist(user, code=400, message="No user found with this card id")

            for a in db.query(UserProductAssociation).filter_by(user_id=user.user_id).all():
                a.count = 0
            db.commit()

        return jsonify(True)
