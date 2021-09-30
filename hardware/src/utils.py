import sys
import os

from datetime import datetime

def log(*args):
    print("[", datetime.now().strftime("%H:%M:%S"), "]", *args)

def is_raspberry ():
    if sys.platform.startswith('win'):
        return False
    elif os.uname().nodename == 'raspberrypi':
        return True
    else:
        return False