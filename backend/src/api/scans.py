from flask import abort, jsonify
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist, authentification_required

from database.database import Database
from database.scan import Scan
from database.user import User

ns = Namespace('scans', description='Card scanning related operations')

SCAN_PARAMS = ns.model('Scan post parameter', {
    "cardUID": fields.String(required=True),
    "transactionValue": fields.Float(required=True)
})

@ns.route('/scan')
class Scans(Resource):
    
    @ns.expect(SCAN_PARAMS, validate=True)
    @authentification_required
    def post(self, **kwargs):

        card_uid = str(ns.payload["cardUID"])
        currency_amount = float(ns.payload["transactionValue"])

        abort_if_doesnt_exist(
            card_uid, 
            currency_amount,
            message="Server could not get parameters properly",
            code=500
        )

        transaction_status = None
        transaction_date = None
        unkown_card = None
        user = None
        card_currency = None

        with Database(auto_commit=True) as db:

            unkown_card = db.query(User).filter_by(
                card_uid=card_uid).count() == 0

            if unkown_card:
                if currency_amount >= 0:
                    user = User(card_uid, currency_amount)
                    transaction_status = "ACCEPTED"
                else:
                    user = User(card_uid, 0)
                    transaction_status = "NEW_USER_CANT_SPEND"
                db.add(user)
            else:
                user = db.query(User).filter_by(card_uid=card_uid).first()
                if user.currency_amount + currency_amount >= 0:
                    user.currency_amount += currency_amount
                    transaction_status = "ACCEPTED"
                else:
                    transaction_status = "NOT_ENOUGH_CURRENCY"

            scan = Scan(card_uid, currency_amount)
            db.add(scan)

            db.commit()

            abort_if_doesnt_exist(
                user, message="Server error : no user found and could not be created", code=500)

            card_currency = user.currency_amount
            transaction_date = str(scan.date)

            abort_if_doesnt_exist(
                transaction_status,
                transaction_date,
                unkown_card,
                user,
                card_currency,
                message="Internal server error, transaction error",
                code=500
            )

            return {
                'userId': user.user_id,
                'newCard': unkown_card,
                'transactionStatus': transaction_status,
                'transactionDate': transaction_date,
                'cardCurrency': card_currency
            }

    @authentification_required
    def get(self, **kwargs):
        last_scans = []
        with Database(auto_commit=True) as db:
            result = db.query(Scan).order_by(Scan.date.desc()).limit(7)
            for scan in result:
                last_scans.append(scan.to_dict())
        return jsonify(last_scans)
