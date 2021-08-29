from flask import abort
from flask_restx import Resource, Namespace

from .utils import abort_if_doesnt_exist

from webargs import fields
from webargs.flaskparser import use_args

from database.database import Database
from database.scan import Scan
from database.user import User

ns = Namespace('scans', description='Card scanning related operations')

SCAN_PARAMS = {
    "cardId": fields.Str(required=True),
    "transactionValue": fields.Float(required=True)
}

@ns.route('/scans')
class Scans(Resource):
    @use_args(SCAN_PARAMS)
    def post(self, params):

        if not params:
            abort(400, 'No parameters provided')

        card_id = params.get('cardId', None)
        currency_amount = params.get('transactionValue', None)

        abort_if_doesnt_exist(card_id, currency_amount,
                              message="Missing parameter")

        transaction_status = None
        transaction_date = None
        unkown_card = None
        user = None
        card_currency = None

        with Database(auto_commit=True) as db:

            unkown_card = db.query(User).filter_by(card_id=card_id).count() == 0

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

            abort_if_doesnt_exist(user, message="Server error : no user found and could not be created", code=500)

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
