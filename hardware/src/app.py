#!/usr/bin/env python3

import eel
import random
import subprocess
from datetime import datetime

# 480,320

# bashCmd = ["chromium-browser", "--kiosk", "http://localhost:8000/"]
# process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)

eel.init('web')

@eel.expose
def get_random_name():
    print("hellow world")
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))

@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')

@eel.expose
def kill():
    # process.terminate()
    print("no kill")

print("start")
eel.start('index.html', mode=None, host='0.0.0.0')
# eel.start('index.html', mode='chrome', cmdline_args=['--window-size=480,320', '--window-position=0,0', '--start-fullscreen', '--kiosk'])
print("done")