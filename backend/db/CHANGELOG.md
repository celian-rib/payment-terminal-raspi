## 09/10/2021 

- Ajout des status de transaction dans la table scans

```ALTER TABLE scans ADD COLUMN "transaction_status" string default null;```