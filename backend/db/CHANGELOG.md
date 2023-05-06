## 09/10/2021 

- Ajout des status de transaction dans la table scans

```ALTER TABLE scans ADD COLUMN "transaction_status" string default null;```


## 11/10/2021 

- Ajout d'une boolean pour admin dans la table users

```ALTER TABLE users ADD COLUMN "admin" boolean default false;```
