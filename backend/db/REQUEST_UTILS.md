# Nombre de scans moyen par jour depuis le début :

```select avg(nb) from (select count(*) as nb, date from scans group by strftime('%Y-%m-%d', date));```

# Dépense moyenne par jour au total :

TO DO

# Dépense moyenne par jour pour un utilisateur

TO DO

# Argent total dépensé sur les 7 derniers jours

TO DO

# 
