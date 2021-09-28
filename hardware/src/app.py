#!/usr/bin/env python3

import eel
import os
import server

print("Starting web server...")

eel.init('web')

@eel.expose
def hello_world():
    print("hellow world from python")
    eel.prompt_alerts('Hello world call from python -> exec on js')

# condition de sortie de await_card_scan
urlOne = None

@eel.expose
def await_card_scan(price):
    print("New transaction started : ", price)

    # on définis les valeurs de l'url à comparer
    urlOne = eel.get_current_url()();
    nameTwo = name = eel.get_current_url()();
    i = 0
    # si l'arret est volontaire ou non
    cancel = 0
    # tant que l'url reste inchangée
    while(True):
        if urlOne != nameTwo:
            cancel = 2
            break;

        nameTwo = name = eel.get_current_url()();
        print("ok", nameTwo, "; name :", urlOne);
        i=i+1
        # au bout de 5 tours arret volontaire
        if i > 5:
            # arret volontaire, true
            cancel = 0
            break
        # une fois par seconde
        eel.sleep(1);
    # transaction terminée
    print("done");
    if cancel == 1:
        eel.scan_complete(450, 465)
    elif cancel == 0:
        eel.scan_cancel(450, 465, "problème sur la lecture de carte")
    else:
        print("User left transaction")

@eel.expose
def get_stats():
    print("Retreiving stats")
    stats = server.get_stats().json()
    print(stats)
    return stats

print("Web server started on port 8000")


if os.uname().nodename == 'raspberrypi':
    eel.start(
        'index.html',
        mode='chrome',
        host='0.0.0.0',
        cmdline_args=[
            '--window-size=480,320',
            '--window-position=0,0',
            '--start-fullscreen',
            '--disable-features=Translate',
            '--kiosk'
        ]
    )
else:
    eel.start(
        'index.html',
        mode=None,
        host='0.0.0.0'
    )

print("Web server terminated")
