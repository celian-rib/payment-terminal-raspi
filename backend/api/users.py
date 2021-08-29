from flask import Flask, jsonify
from flask_restx import Api, Resource, Namespace
from database.user import User
from database.database import Database

ns = Namespace('users', description='Users related operations')

@ns.route('/user')
class UserQuery(Resource):

	def get(self):
		user_list = []
		with Database(auto_commit=True) as db :
			result = db.query(User).all()
			for user in result :
				user_list.append(user.to_dict())
		return jsonify(user_list)

	def post(self):
		return "TO DO CREATE USER"

