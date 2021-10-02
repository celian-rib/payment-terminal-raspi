import requests
import os
import smtplib
import socket

from datetime import datetime
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64

BACKUP_MAIL_ADDRESS = "celian.riboulet@gmail.com"

DB_PATH = str(Path(__file__).parent.parent) + "/db/prod.sqlite3"

def internet_on():
    try:
        requests.get('https://www.google.com/', timeout=1)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

def send_backup():
    print("Sending new backup...")
    SUBJECT = "Asso-Card Backup " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = BACKUP_MAIL_ADDRESS
    msg['To'] = BACKUP_MAIL_ADDRESS

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(DB_PATH, "rb").read())
    encode_base64(part)
    part.add_header(
        'Content-Disposition',
        'attachment; filename="backup.sqlite3"'
    )

    msg.attach(part)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(BACKUP_MAIL_ADDRESS, os.environ.get('SMTP_PASSWORD'))

    session.sendmail(BACKUP_MAIL_ADDRESS, BACKUP_MAIL_ADDRESS, msg.as_string())

    print("Backup sent to ", BACKUP_MAIL_ADDRESS)

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
        print("BACKUP ERROR", e)
