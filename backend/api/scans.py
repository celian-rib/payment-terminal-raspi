from flask import abort
from .utils import abort_if_doesnt_exist
from flask_restx import Resource, Namespace

from webargs import fields
from webargs.flaskparser import use_args

from database.database import Database
from database.scan import Scan

ns = Namespace('scans', description='Card scanning related operations')

SCAN_PARAMS = {
    "cardId": fields.Str(required=True),
    "transactionValue": fields.Int(required=True)
}

@ns.route('/scans')
class Scans(Resource):
    @use_args(SCAN_PARAMS)
    def post(self, params):

        if not params:
            abort(400, 'No parameters provided')

        card_id = params.get('cardId', None)
        currency_amount = params.get('transactionValue', None)
    
        abort_if_doesnt_exist(card_id, currency_amount, message="Missing parameter")
        unkown_card = True

        with Database(auto_commit=True) as db :
            # On ajoute ce scan à la base de donnée
            scan = Scan(card_id, currency_amount)
            db.add(scan)
            db.commit()

            # On cherche si cette carte est déjà connu
            unkown_card = db.query(Scan).filter_by(card_id=card_id).count() == 0

            # if unkown_card :
                
        return {
            'newCard': unkown_card,
            'transactionAccepted': True
        }