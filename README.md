# Asso-Card Project :

A payment terminal working with a touchscreen and an NFC reader mounted on a Raspberry PI. The goal is to handle money transaction at the students' desk snaks shop at the IUT of Bordeaux.

Everything is self hosted into the raspberry and does not require an internet connection.

## Structure :

Asso-Card is composed of two sub-project

### Backend :

Handling a Flask application running the database.

**Hosted into the raspberry**

### Hardware :

Python web server + vanilla static web site.


## ENV file setup :

```
AUTH_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SFTP_HOST ="info-ssh1.iut.u-bordeaux.fr"
SFTP_USERNAME ="<iutuser>"
SFTP_HOST_PATH ="/mnt/roost/users/<iutuser>/<backupfolder>"
SFTP_KEY="xxxxxxxxxx"
```
> SFTP related keys are for the backup system.
