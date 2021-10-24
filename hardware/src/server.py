
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
    return requests.post(url=BACKEND_URL + "/api/scan", headers=HEADERS, json=payload)

def get_stats():
    return requests.get(url=BACKEND_URL + "/api/stats", headers=HEADERS)

def get_historic(count):
    return requests.get(url=BACKEND_URL + "/api/scans/" + str(count), headers=HEADERS)

def user_is_admin(card_uid):
    response = requests.get(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS)
    return response.json()["admin"]

def get_user(card_uid):
    return requests.get(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS)

def post_debt_amount(card_uid, debt_update_amount):
    payload = {
        'debt_update_amount': debt_update_amount
    }
    return requests.post(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), json=payload)