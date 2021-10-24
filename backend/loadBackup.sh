#!/bin/bash

green=`tput setaf 2`
cyan=`tput setaf 6`
reset=`tput sgr0`

echo "$cyan Retreiving todays backup from server...$reset"
rsync -tuP criboulet@info-ssh1.iut.u-bordeaux.fr:"~/asso-card-backups/*$(date +"%d_%m")*.sqlite3" ./db/dev.sqlite3
echo "$green Done $reset"