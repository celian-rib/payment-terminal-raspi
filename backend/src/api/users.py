from flask import Flask, jsonify
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist

from database.user import User
from database.database import Database
from datetime import datetime

ns = Namespace('users', description='Users related operations')


@ns.route('/users')
class Users(Resource):
    def get(self):
        user_list = []
        with Database(auto_commit=True) as db:
            result = db.query(User).all()
            for user in result:
                user_list.append(user.to_dict())
        return jsonify(user_list)


USER_UPDATE_PARAMS = ns.model('Updating user parameter', {
    "name": fields.String(required=True),
    "firstName": fields.String(required=True),
    "email": fields.String(required=True)
})

@ns.route('/user/<card_uid>')
class SingleUser(Resource):
    def get(self, card_uid):
        user = None

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            if user:
                user = user.to_dict()

        abort_if_doesnt_exist(
            user, code=400, message="No user found with this card id")

        return jsonify(user)

    @ns.expect(USER_UPDATE_PARAMS, validate=True)
    def post(self, card_uid, **kwargs):
        name = str(ns.payload["name"])
        first_name = str(ns.payload["firstName"])
        email = str(ns.payload["email"])

        abort_if_doesnt_exist(
            name, 
            first_name,
            email,
            message="Server could not get parameters properly",
            code=500
        )

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            abort_if_doesnt_exist(user, code=400, message="No user found with this card id")

            user.update_date = datetime.now()
            user.name = name
            user.first_name = first_name
            user.email = email
            db.commit()

        return True