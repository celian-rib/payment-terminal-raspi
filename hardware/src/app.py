#!/usr/bin/env python3

import eel
from sys import platform

print("Starting web server...")

eel.init('web')


@eel.expose
def hello_world():
    print("hellow world from python")
    eel.prompt_alerts('Hello world call from python -> exec on js')


print("Web server started on port 8000")

if platform == "linux" or platform == "linux2":
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
