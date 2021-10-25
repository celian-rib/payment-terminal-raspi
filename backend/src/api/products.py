from flask import abort, jsonify
from flask_restx import Resource, Namespace, fields
from sqlalchemy.sql.functions import func

from .utils import abort_if_doesnt_exist, authentification_required

from database.database import Database
from database.user import User
from database.product import Product, UserProductAssociation

ns = Namespace('products', description='Selling products')


@ns.route('/products')
class Products(Resource):
    def get(self):
        products = []
        with Database(auto_commit=True) as db:
            for p in db.query(Product).all():
                products.append(p.to_dict())
        return jsonify(products)

    def patch(self):
        products = [
            {"name": "Boisson", "price": 60, "color": "#f6e58d"},
            {"name": "Twix", "price": 40, "color": "#55efc4"},
            {"name": "Bueno", "price": 70, "color": "#c7ecee"},
            {"name": "Smarties", "price": 60, "color": "#686de0"},
            {"name": "PastaBox", "price": 220, "color": "#fab1a0"},
            {"name": "Riz", "price": 170, "color": "#c7ecee"},
            {"name": "Sandwich", "price": 170, "color": "#c7ecee"},
            {"name": "Cafés", "price": 40, "color": "#778beb"},
            {"name": "Lion", "price": 40, "color": "#ffbe76"},
            {"name": "Gauffre Sucre", "price": 40, "color": "#ffbe76"},
            {"name": "Gauffre Choco", "price": 50, "color": "#e17055"},
            {"name": "Bounty", "price": 50, "color": "#81ecec"},
            {"name": "Snickers", "price": 50, "color": "#e17055"},
            {"name": "Chips", "price": 70, "color": "#c7ecee"},
            {"name": "Monster", "price": 120, "color": "#cf6a87"},
            {"name": "PomPote", "price": 40, "color": "#55efc4"},
            {"name": "Bready", "price": 70, "color": "#c7ecee"},
            {"name": "Nestle", "price": 60, "color": "#f9ca24"},
            {"name": "Crunch", "price": 60, "color": "#a29bfe"},
            {"name": "KitKat", "price": 60, "color": "#a29bfe"},
            {"name": "M&Ms", "price": 60, "color": "#a29bfe"},
            {"name": "Dragibus", "price": 50, "color": "#81ecec"},
            {"name": "Caprisun", "price": 30, "color": "#ffeaa7"},
            {"name": "PastaXtrem", "price": 370, "color": "#f5cd79"},
            {"name": "Nouilles", "price": 110, "color": "#ea8685"},
        ]
        with Database(auto_commit=True) as db:
            for p in products:
                if db.query(Product).filter_by(name=p["name"]).count() > 0:
                    product = db.query(Product).filter_by(
                        name=p["name"]).first()
                    product.name = p["name"]
                    product.asso_price = p["price"]
                    product.color = p["color"]
                    continue
                product = Product(p["name"], p["price"], p["color"])
                db.add(product)
            db.commit()

        return True


USER_PRODUCTS_UPDATE_PARAMS = ns.model('Updating user products parameter', {
    "product_id": fields.Integer(required=True),
    "adding": fields.Boolean(required=True),
})


@ns.route('/products/user/<card_uid>')
class UserProducts(Resource):
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
                product_association = db.query(UserProductAssociation).filter_by(user_id=user.user_id).filter_by(product_id=product_id).first()
                if not product_association:
                    product_association = UserProductAssociation(product_id=product_id, user_id=user.user_id, count=1, product=product)
                else:
                    product_association.count += 1
                user.products.append(product_association)
            else:
                product_association = db.query(UserProductAssociation).filter_by(user_id=user.user_id).filter_by(product_id=product_id).first()
                if product_association.count > 0:
                    product_association.count -= 1
                user.products.append(product_association)
            db.commit()

        return jsonify(True)

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
