
import os

import os
import requests

from dotenv import load_dotenv
from utils import log

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
    try:
        return requests.get(url=BACKEND_URL + "/api/stats", headers=HEADERS)
    except:
        log("Error while retreiving stats...")
        return None


def get_historic(count):
    try:
        return requests.get(url=BACKEND_URL + "/api/scans/" + str(count), headers=HEADERS)
    except:
        log("Error while retreiving historic...")
        return None

def get_products():
    try:
        return requests.get(url=BACKEND_URL + "/api/products" , headers=HEADERS)
    except:
        log("Error while retreiving products...")
        return None

def add_or_remove_user_product(card_uid, product_id, adding):
    payload = {
        'product_id': product_id,
        'adding': adding
    }
    requests.put(url=BACKEND_URL + "/api/products/user/" + str(card_uid), headers=HEADERS, json=payload)

def user_is_admin(card_uid):
    try:
        response = requests.get(
            url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS)
        return response.json()["admin"]
    except:
        log("Error while retreiving user...")
        return None


def get_user(card_uid):
    try:
        return requests.get(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS)
    except:
        log("Error while retreiving user...")
        return None

def delete_all_user_products(card_uid):
    requests.delete(url=BACKEND_URL + "/api/products/user/" + str(card_uid), headers=HEADERS)