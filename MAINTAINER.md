## Installer le projet (Pour développer dessus)

Le projet est séparé en 2 sous-modules :

- backend -> api flask + bd sqlite

- hardware -> wrapper python pour le rfid + frontend vanilla javascript

Les dossier de chacun de ces modules possèdent des README expliquant leur installation.

1. Start back:

```cd ./backend && python3 src/app.py```

2. Start front:

```cd ./hardware/src && python3 app.py```


## Modifier / Ajouter / Supprimer les consos Asso

> Le système de consos asso implique d'avoir les élèments en vente stocké dans la bd (table "products")

Pour mettre à jour les produits il faut modifier puis lancer le script [products.sql](./backend/db/products.sql)
```
sqlite3 fichierdelabd.sqlite3 < products.sql
```

## Ajouter un membre Asso (administrateur)

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


