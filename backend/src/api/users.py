from flask import Flask, jsonify
from flask_restx import Api, Resource, Namespace

from .utils import abort_if_doesnt_exist

from database.user import User
from database.database import Database

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


@ns.route('/user/<card_uid>')
class SignelUser(Resource):
    def get(self, card_uid):
        user = None

        with Database(auto_commit=True) as db:
            user = db.query(User).filter_by(card_uid=card_uid).first()
            if user:
                user = user.to_dict()

        abort_if_doesnt_exist(
            user, code=400, message="No user found with this card id")

        return jsonify(user)
