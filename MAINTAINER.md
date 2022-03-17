## Installer le projet (Pour développer dessus)

Le projet est séparé en 2 sous-modules :

- backend -> api flask + bd sqlite

- hardware -> wrapper python pour le rfid + frontend vanilla javascript

Les dossier de chacun de ces modules possèdent des README expliquant leur installation.

1. Start back:

```cd ./backend && python3 src/app.py```

2. Start front:

```cd ./hardware/src && python3 app.py```

## Bases de données

Il existe 2 base de données :

- dev.sqlite3 -> base de développement qui ne risque rien
- prod.sqlite3 -> base de prod **HYPER CRITIQUE, IL Y A DE L'ARGENT DEDANS**

La base prod.sqlite3 est normalement que dans la version du projet qui est dans la raspberry pi, donc durant toute manip de la raspberry (à travers ssh ou autre), il faut faire très attention à ce fichier !!!!

## Modifier / Ajouter / Supprimer des produits de consos Asso

> Le système de consos asso implique d'avoir les élèments en vente stockés dans la bd (table "products")

Pour mettre à jour les produits il faut modifier puis lancer le script [products.sql](./backend/db/products.sql)
```
sqlite3 fichierdelabd.sqlite3 < products.sql
```

## Ajouter un membre Asso (Pour les consos asso)

1. Se connecter en ssh à la raspberry pi (Cela implique qu'elle soit sur un réseau wifi connu)
- Utilisateur : `pi`
- Mot de passe : demander à quelqu'un qui le sait

2. Aller dans `~/asso-card/backend/db`

3. `sqlite3 prod.sqlite3` pour ouvrir la bd

- Pour rendre plus lisible sqlite : `.header on` puis `.mode column`

4. Mettre `admin` à 1 pour la personne concernée (+ Ajouter les infos perso : nom et prénom)

```sql
update users 
set name = "NOM", first_name = "PRENOM", admin = 1 where user_id = <ID DE LA PERSONNE>;
```

## Ajouter un réseaux wifi

TODO

## Comment fonctionne la raspberry 

Après le lancement

- Si la raspberry est connectée à internet, elle pull la dernière version de la branche main
- Lancement du backend
- Lancement du front-end
- Lancement de chromium et ouverture de la page web
