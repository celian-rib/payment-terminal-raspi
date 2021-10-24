import eel
import server
import gevent
import requests

from utils import log, is_raspberry
pn532 = None

if is_raspberry():
    from py532lib.i2c import *
    from py532lib.frame import *
    from py532lib.constants import *

    pn532 = Pn532_i2c()
    pn532.SAMconfigure()


def get_uid_string(byte_list) -> str:
    uid = ""
    for i in byte_list:
        uid += str(i)
    return uid


def read_scanner():
    if not pn532:
        # artificial scan
        delay = 2
        log("[ non-pi development server detected ]")
        log("[ SIMULATING SCAN IN", delay, "SEC]")
        eel.sleep(delay)
        return [10, 20, 30, 40, 50, 60]
    return pn532.read_mifare().get_data()


def await_card_scan(price):
    card_data = read_scanner()  # blocking call
    card_uid = get_uid_string(list(card_data))
    log("[ CARD FOUND ] uid :", card_uid)

    transaction_data = None
    try:
        transaction_data = server.send_scan(card_uid, float(price)).json()
        log("Transaction result : ", transaction_data)
    except Exception as e:
        if isinstance(e, requests.ConnectionError):
            log("[ Request Error !! ]")
            eel.scan_cancel(
                0, 0, "La transaction n'a pas pu être envoyée au serveur...")
        else:
            log("[ Request Error !! ]", e)
            eel.scan_cancel(
                0, 0, "Erreur inconnue durant l'envois de la transaction...")
        return

    transaction_status = transaction_data["transactionStatus"]
    card_currency = transaction_data["cardCurrency"]
    user_id = transaction_data["userId"]

    if transaction_status == "ACCEPTED":
        eel.scan_complete(card_currency, user_id)
    else:
        eel.scan_cancel(card_currency, user_id, transaction_status)

@eel.expose
def start_transaction(price):
    log("New transaction started:", price)

    # start scan in background
    async_scan = eel.spawn(await_card_scan, price)
    while (True):
        loaded_url = None
        try:
            loaded_url = eel.get_current_url()()
        except:
            loaded_url = "nfc"
        if "nfc" not in str(loaded_url) :
            log("[ CLOSED ] The transaction is closed")
            gevent.kill(async_scan)
            break
        eel.sleep(1)
        log(loaded_url)

@eel.expose
def start_admin_validation():
    log("New scan started:")
    card_data = read_scanner()  # blocking call
    card_uid = get_uid_string(list(card_data))
    return {
        "admin": server.user_is_admin(card_uid),
        "card_uid": card_uid
    }

@eel.expose
def get_user(card_uid):
    log("Retreiving user")
    try:
        user = server.get_user(card_uid).json()
        return user
    except:
        log("Error while retreiving user...")
        return None

@eel.expose
def get_stats():
    log("Retreiving stats")
    try:
        stats = server.get_stats().json()
        return stats
    except:
        log("Error while retreiving stats...")
        return None

@eel.expose
def get_historic():
    log("Retreiving historic")
    try:
        historic = server.get_historic(5).json()
        return historic
    except:
        log("Error while retreiving historic...")
        return None

@eel.expose
def update_debt(card_uid, debt_update_amount):
    log("Updating dept")
    try:
        debt_amount = server.post_debt_amount(card_uid, debt_update_amount).json()
        return debt_amount
    except:
        log("Error while updating dept...")
        return None