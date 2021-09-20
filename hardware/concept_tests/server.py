import requests
import json

URL = "http://127.0.0.1:5000"


def send_scan(card_uid, transaction_value):
    payload = {
        "cardId": card_uid,
        "transactionValue": transaction_value
    }
    return requests.post(URL + "/api/scans", json=payload)

def get_user_info(card_uid):
    return requests.get(URL+ "/api/user/" + card_uid)
