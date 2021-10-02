import eel
import server
import gevent

from utils import log, is_raspberry
from requests.exceptions import ConnectionError

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
        delay = 5
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
        if isinstance(e, ConnectionError):
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

    # Check for transaction end (If page has been changed by the user or by an ending transaction)
    current_loaded_url = eel.get_current_url()()
    buffer_url = current_loaded_url
    while (True):
        if current_loaded_url != buffer_url:
            log("[ CLOSED ] The transaction is closed")
            gevent.kill(async_scan)
            break
        current_loaded_url = eel.get_current_url()()
        eel.sleep(0.5)


@eel.expose
def get_stats():
    log("Retreiving stats")
    try:
        stats = server.get_stats().json()
        log(stats)
        return stats
    except:
        log("Error while retreiving stats...")
        return None
