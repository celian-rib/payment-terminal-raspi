## Setup

Installer python3

Installer tous les modules python
```pip3 install -r requirement.txt```


## Start backend

```python3 src/app.py``` (From folder "backend")

## Manual database edition

```sqlite3 <path to file slite3>```

Check tables : ```.table```

SQL exec : ```<CMD SQL> ;```

Ex : ```SELECT * FROM SCANS;```

## Add attribute to the table

```ALTER TABLE <table> ADD COLUMN "nom_col" BOOLEAN DEFAULT FALSE```

### ADD THE CHANGE TO THE CHANGELOG.MD file

## Mettre à jour le requirement.txt

```pip3 freeze > requirement.txt``` (From folder "backend")


## Build docker image

```docker image build -t backend .``` (From folder "backend")

## Run docker image

```docker run -p 5000:5000 -v $(pwd)/db:/usr/src/app/db -d backend``` (From folder "backend")

## Explore docker container

```docker exec -t -i <container> /bin/bash```