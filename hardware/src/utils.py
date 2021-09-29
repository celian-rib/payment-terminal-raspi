from datetime import datetime

def log(*args):
    print("[", datetime.now().strftime("%H:%M:%S"), "]", *args)