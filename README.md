# Asso-Card Project :

## Fichier ENV :

```
AUTH_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SFTP_HOST ="info-ssh1.iut.u-bordeaux.fr"
SFTP_USERNAME ="<iutuser>"
SFTP_HOST_PATH ="/mnt/roost/users/<iutuser>/<backupfolder>"
SFTP_KEY="xxxxxxxxxx"
```

AUTH_TOKEN: utile dans le cas ou le backend devrait être externalisé (L'API est donc déjà sécurisée)
SFTP_... : utile pour les backup via sftp envoyées sur le serveur de l'iut (sur criboulet)


## Lancer le projet (Serveurs de développement)

Lancer front:

```cd ./hardware/src && python3 app.py```

Lancer back:

```cd ./backend && python3 src/app.py```

