import requests
import os
import socket
import pysftp

from pathlib import Path
from cryptography.fernet import Fernet

DB_PATH = str(Path(__file__).parent.parent) + "/db/prod.sqlite3"

def internet_on():
    try:
        requests.get("https://google.com", timeout=1)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

def send_backup():
    print("Sending new backup...")
    key = list(os.environ.get('SFTP_PRIVATE_KEY'))
    print(bytes(key))
    fernet = Fernet(bytes(key))
    host=os.environ.get('SFTP_HOST')
    user=os.environ.get('SFTP_USERNAME')
    pswd = fernet.decrypt(os.environ.get('SFTP_AUTH_CHAIN')).decode()
    with pysftp.Connection(
        host=host,
        username=user, 
        password=pswd
    ) as sftp:
        sftp.put(DB_PATH, os.environ.get('SFTP_HOST_PATH'))

    print("Backup sent to ", host)

def check_if_backup_required():
    if not internet_on():
        print("Backup check canceled : NO INTERNET")
        return

    # local_ip = str(socket.gethostbyname(socket.gethostname()))
    # if local_ip == "192.168.1.29" or local_ip == "192.168.1.37":
    #     print("Backup canceled : Celian's home detected")
    #     return
    
    try:
        send_backup()
    except Exception as e:
        print("[ BACKUP ERROR ]", e)
