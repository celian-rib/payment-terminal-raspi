from flask import abort, jsonify
from flask_restx import Resource, Namespace, fields
from sqlalchemy.sql.functions import func

from .utils import abort_if_doesnt_exist, authentification_required

from database.database import Database
from database.scan import Scan
from database.user import User

ns = Namespace('leaderboard', description='Users leaderboard')

@ns.route('/leaderboard')
class Leaderboard(Resource):
    @authentification_required
    def get(self, **kwargs):

        with Database(auto_commit=True) as db:
            users = db.query(User).filter_by(admin=False).all()
            users_scores = []

            for user in users:
                user.card_uid
                raw_score = db.query(func.sum(Scan.currency_amount))\
                    .filter_by(card_uid=user.card_uid)\
                    .filter(Scan.currency_amount < 0)\
                    .filter_by(transaction_status="ACCEPTED").all()[0][0]
                score = abs(raw_score) if raw_score != None else 0
                users_scores.append({
                    "user": user.to_dict(),
                    "score": score
                })
            
        users_scores = sorted(users_scores, key=lambda d: d['score'], reverse=True)

        return jsonify(users_scores)