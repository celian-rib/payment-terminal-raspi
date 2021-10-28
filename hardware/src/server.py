
import os
import eel
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


def user_is_admin(card_uid):
    try:
        response = requests.get(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS)
        return response.json()["admin"]
    except Exception as e:
        log("Error while retreiving user adminity...", e)
        return None


@eel.expose
def get_stats():
    try:
        return requests.get(url=BACKEND_URL + "/api/stats", headers=HEADERS).json()
    except Exception as e:
        log("Error while retreiving stats...", e)
        return None


@eel.expose
def get_historic():
    try:
        return requests.get(url=BACKEND_URL + "/api/scans/" + str(5), headers=HEADERS).json()
    except Exception as e:
        log("Error while retreiving historic...", e)
        return None


@eel.expose
def get_products():
    try:
        return requests.get(url=BACKEND_URL + "/api/products", headers=HEADERS).json()
    except Exception as e:
        log("Error while retreiving products...", e)
        return None


@eel.expose
def add_or_remove_user_product(card_uid, product_id, adding):
    try:
        payload = {
            'product_id': product_id,
            'adding': adding
        }
        requests.put(url=BACKEND_URL + "/api/products/user/" + str(card_uid), headers=HEADERS, json=payload)
    except Exception as e:
        log("Error while editing user products...", e)


@eel.expose
def get_user(card_uid):
    try:
        return requests.get(url=BACKEND_URL + "/api/user/card_uid/" + str(card_uid), headers=HEADERS).json()
    except Exception as e:
        log("Error while retreiving user...", e)
        return None


@eel.expose
def delete_all_user_products(card_uid):
    try:
        requests.delete(url=BACKEND_URL + "/api/products/user/" + str(card_uid), headers=HEADERS)
    except Exception as e:
        log("Error while deleting all user products...", e)
