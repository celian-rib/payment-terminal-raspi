
import os

import os
import requests

from dotenv import load_dotenv
load_dotenv()

BACKEND_URL = "http://127.0.0.1:5000"
HEADERS = {"x-access-tokens": os.environ.get("AUTH_TOKEN")}

def send_scan(card_uid, transaction_value):
    payload = {
        'cardUID': card_uid,
        'transactionValue': transaction_value
    }
    return requests.post(url=BACKEND_URL + "/api/scan", json=payload)

def get_stats():
    return requests.get(url=BACKEND_URL + "/api/stats")