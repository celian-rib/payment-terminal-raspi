#!/usr/bin/env python3

import eel
import random
import subprocess
from datetime import datetime

print("Starting web server...")

# 480,320

# bashCmd = ["chromium-browser", "--kiosk", "http://localhost:8000/"]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)

eel.init('web')

@eel.expose
def hello_world():
    print("hellow world from python")
    eel.prompt_alerts('Hello world call from python -> exec on js')

@eel.expose
def debut_transaction(price):
    print(price)
    eel.go_to_wait()


print("Web server started on port 8000")

eel.start('./index.html', mode=None, host='0.0.0.0')
# eel.start('index.html', mode='chrome', host='0.0.0.0', cmdline_args=['--window-size=480,320', '--window-position=0,0', '--start-fullscreen', '--disable-features=Translate', '--kiosk'])
print("Web server terminated")