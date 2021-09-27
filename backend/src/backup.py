import requests
import os
import smtplib

from datetime import datetime
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64

BACKUP_MAIL_ADDRESS = "celian.riboulet@gmail.com"
BACKUP_INTERVAL_HOURS = 1;

FILE_NAME = str(Path(__file__).parent) + "/.backup_timestamp"
DB_PATH = str(Path(__file__).parent.parent) + "/db/dev.sqlite3"

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
    session.login(BACKUP_MAIL_ADDRESS, "kifmmylkvwrendzq")

    session.sendmail(BACKUP_MAIL_ADDRESS, BACKUP_MAIL_ADDRESS, msg.as_string())

    with open(FILE_NAME, "w+") as f:
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    print("Backup sent to ", BACKUP_MAIL_ADDRESS)

def check_if_backup_required():
    if not internet_on():
        print("Backup check canceled : NO INTERNET")
        return;
    try:
        with open(FILE_NAME, "r+") as f:
            time_str = f.readline()
            last_backup = datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S")
            delta = datetime.now() - last_backup
            print("Last database backup : ", last_backup)
            print("Delay since last backup : ", delta)

            if delta.total_seconds() >= BACKUP_INTERVAL_HOURS * 60 * 60:
                send_backup() 
    except:
        print("No backup timestamp file found, a new one will be created")
