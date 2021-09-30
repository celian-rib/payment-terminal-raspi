# nb total user
# nb total d'argent cumulé dans la système
# nb total de scan

from flask import Flask, jsonify
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist, authentification_required

from database.scan import Scan
from database.user import User
from database.database import Database
from datetime import datetime

ns = Namespace('stats', description='User and currency stats')

@ns.route('/stats')
class Stats(Resource):
    @authentification_required
    def get(self):
        total_user = 0
        total_stored_currency = 0
        total_scan_count = 0
        with Database(auto_commit=True) as db:
            users = db.query(User).all()
            total_user = len(users)
            for u in users:
                total_stored_currency += u.currency_amount
            total_scan_count = db.query(Scan).count()

        return {
            'totalUsers': total_user,
            'totalStoredCurrency': total_stored_currency,
            'totalScanCount': total_scan_count
        }