import eel
import server

from utils import log, is_raspberry
from requests.exceptions import ConnectionError

pn532 = None

if is_raspberry():
    from py532lib.i2c import *
    from py532lib.frame import *
    from py532lib.constants import *

    pn532 = Pn532_i2c()
    pn532.SAMconfigure()

# condition de sortie de await_card_scan
current_loaded_url = None

def get_uid_string(byte_list) -> str:
    uid = "" 
    for i in byte_list:
        uid += str(i)
    return uid

# def async_card_scan():
#     card_data = pn532.read_mifare().get_data()
#     print(card_data)

@eel.expose
def await_card_scan(price):
    log("New transaction started:", price)

    card_data = None
    if not pn532 :
        # artificial scan
        log("[ non-pi development server detected ]")
        log("[ SIMULATING SCAN IN 2SEC]")
        eel.sleep(2)
        card_data = [10, 20, 30, 40, 50, 60]
    else :
        card_data = pn532.read_mifare().get_data()
    
    card_uid = get_uid_string(list(card_data))
    log("Card uid :", card_uid)
    
    transaction_data = None
    try:
        transaction_data = server.send_scan(card_uid, float(price)).json()
        log("Transaction result : ", transaction_data)
    except Exception as e:
        if isinstance(e, ConnectionError):
            log("[ Request Error !! ]")
            eel.scan_cancel(0, 0, "La transaction pa pu être envoyée au serveur...")
        else:
            log("[ Request Error !! ]", e)
            eel.scan_cancel(0, 0, "Erreur inconnue durant l'envois de la transaction...")
        return

    transaction_status = transaction_data["transactionStatus"]
    card_currency = transaction_data["cardCurrency"]
    user_id = transaction_data["userId"]

    if transaction_status == "ACCEPTED":
        eel.scan_complete(card_currency, user_id)
    else:
        eel.scan_cancel(card_currency, user_id, transaction_status)

@eel.expose
def get_stats():
    log("Retreiving stats")
    try :
        stats = server.get_stats().json()
        log(stats)
        return stats
    except :
        log("Error while retreiving stats...")
        return None