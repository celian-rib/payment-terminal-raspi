from flask import abort
from flask_restx import Resource, Namespace, fields

from .utils import abort_if_doesnt_exist

from database.database import Database
from database.scan import Scan
from database.user import User

ns = Namespace('scans', description='Card scanning related operations')

SCAN_PARAMS = ns.model('Scan post parameter', {
    "cardId": fields.String(required=True),
    "transactionValue": fields.Float(required=True)
})

@ns.route('/scans')
class Scans(Resource):
    @ns.expect(SCAN_PARAMS, validate=True)
    def post(self, **kwargs):

        card_id = str(ns.payload["cardId"])
        currency_amount = float(ns.payload["transactionValue"])

        abort_if_doesnt_exist(
            card_id, 
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
                card_id=card_id).count() == 0

            if unkown_card:
                if currency_amount >= 0:
                    user = User(card_id, currency_amount)
                    transaction_status = "ACCEPTED"
                else:
                    user = User(card_id, 0)
                    transaction_status = "NEW_USER_CANT_SPEND"
                db.add(user)
            else:
                user = db.query(User).filter_by(card_id=card_id).first()
                if user.currency_amount + currency_amount >= 0:
                    user.currency_amount += currency_amount
                    transaction_status = "ACCEPTED"
                else:
                    transaction_status = "NOT_ENOUGH_CURRENCY"

            scan = Scan(card_id, currency_amount)
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
            'newCard': unkown_card,
            'transactionStatus': transaction_status,
            'transactionDate': transaction_date,
            'cardCurrency': card_currency
        }
