### Setup

Installer python3

Installer tous les modules python
```pip install -r requirement.txt```


## Start backend

```python3 app.py```


## Tester un endpoint

Comment tester une requète sur un endpoint de l'api (Ex: http://localhost/api/scans)

- Avec la commande curl :

    ```curl http://127.0.0.1:5000/api/users -X GET```

- Avec l'application postman


## Entrer manuellement dans la bd

```sqlite3 <path vers le fichier slite3>```

Voir les tables présentes : ```.table```

Executer du SQL : ```<CMD SQL> ;```

Ex : ```SELECT * FROM SCANS;```


## Mettre à jour le requirement.txt

```pip3 freeze > requirement.txt```