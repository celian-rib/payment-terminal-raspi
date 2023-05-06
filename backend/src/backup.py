import requests
import os
import socket
import pysftp
import base64

from pathlib import Path
from datetime import datetime

DB_PATH = str(Path(__file__).parent.parent) + "/db/prod.sqlite3"

def internet_on():
    try:
        requests.get("https://google.com")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


def send_backup():
    print("Sending new backup...")
    with pysftp.Connection(
        host=os.environ.get('SFTP_HOST'),
        username=os.environ.get('SFTP_USERNAME'),
        password=base64.b64decode(os.environ.get("SFTP_KEY"))
    ) as sftp:
        date = datetime.now().strftime("%Y_%m_%d_%H:%M:%S")
        backup_file = os.environ.get('SFTP_HOST_PATH') + '/db_' + date + '.sqlite3'
        sftp.put(DB_PATH, backup_file)

    print("Backup sent to ", os.environ.get('SFTP_HOST'))


def check_if_backup_required():
    if not internet_on():
        print("Backup check canceled : NO INTERNET")
        return

    local_ip = str(socket.gethostbyname(socket.gethostname()))
    if local_ip == "192.168.1.29" or local_ip == "192.168.1.37":
        print("Backup canceled : Celian's home detected")
        return

    try:
        send_backup()
    except Exception as e:
        print("[ BACKUP ERROR ]", e)
