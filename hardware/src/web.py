import eel;
import server

from utils import log

# condition de sortie de await_card_scan
current_loaded_url = None

@eel.expose
def await_card_scan(price):
    log("New transaction started:", price)

    # on définis les valeurs de l'url à comparer
    current_loaded_url = eel.get_current_url()();
    buffer_url = eel.get_current_url()();
    i = 0
    # si l'arret est volontaire ou non
    cancel = 0
    # tant que l'url reste inchangée
    while(True):
        if current_loaded_url != buffer_url:
            cancel = 2
            break;

        buffer_url = eel.get_current_url()();
        log("[ OK ] Still waiting...");
        i=i+1
        # au bout de 5 tours arret volontaire
        if i > 5:
            # arret volontaire, true
            cancel = 1
            break
        eel.sleep(0.5);

    if cancel == 1:
        log("[ SUCCESS ] Transaction done:", price);
        eel.scan_complete(450, 465)
    elif cancel == 0:
        log("[ ERROR ] reason to do");
        eel.scan_cancel(450, 465, "problème sur la lecture de carte")
    else:
        log("[ CLOSED ] The transaction has been canceled");

@eel.expose
def get_stats():
    log("Retreiving stats")
    stats = server.get_stats().json()
    log(stats)
    return stats