import eel
import server

from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

from utils import log

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
    card_data = pn532.read_mifare().get_data()
    card_uid = get_uid_string(list(card_data))
    
    log("Card uid :", card_uid)
    
    eel.scan_complete(price, card_uid) # A ENLEVR

    # # on définis les valeurs de l'url à comparer
    # current_loaded_url = eel.get_current_url()();
    # buffer_url = eel.get_current_url()();
    # i = 0
    # # si l'arret est volontaire ou non
    # cancel = 0
    # # tant que l'url reste inchangée
    # while(True):
    #     if current_loaded_url != buffer_url:
    #         cancel = 2
    #         break;

    #     card_data = pn532.read_mifare().get_data()

    #     buffer_url = eel.get_current_url()();
    #     log("[ OK ] Still waiting...");
    #     i=i+1
    #     # au bout de 5 tours arret volontaire
    #     if i > 5:
    #         # arret volontaire, true
    #         cancel = 1
    #         break
    #     eel.sleep(0.5);

    # if cancel == 1:
    #     log("[ SUCCESS ] Transaction done:", price);
    #     eel.scan_complete(450, 465)
    # elif cancel == 0:
    #     log("[ ERROR ] reason to do");
    #     eel.scan_cancel(450, 465, "problème sur la lecture de carte")
    # else:
    #     log("[ CLOSED ] The transaction has been canceled");

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