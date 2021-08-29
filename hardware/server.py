import requests
import json

URL = "http://127.0.0.1:5000"


def send_scan(card_id, transaction_value):
    payload = {
        "cardId": card_id,
        "transactionValue": transaction_value
    }
    return requests.post(URL + "/api/scans", json=payload)
