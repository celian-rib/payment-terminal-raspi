# Nombre de scans moyen par jour depuis le début :

```select avg(nb) from (select count(*) as nb, date from scans group by strftime('%Y-%m-%d', date));```

# Dépense moyenne par jour au total :

select avg(nb) / 100 as '€ spend avg per day' from 
(   select SUM(currency_amount) as nb, date 
    from scans 
    where currency_amount < 0 and transaction_status = 'ACCEPTED' 
    group by strftime('%Y-%m-%d', date)
);

# Dépense moyenne par jour pour un utilisateur

select avg(nb) / 100 as '€ spend avg per day by one active user' from 
(   select SUM(currency_amount) as nb, date, card_uid
    from scans 
    where currency_amount < 0 and transaction_status = 'ACCEPTED'
    group by strftime('%Y-%m-%d', date), card_uid
);

# Argent total dépensé sur les 7 derniers jours

select SUM(currency_amount) / 100 from scans
where date > date('now','-7 days') and transaction_status = 'ACCEPTED' and currency_amount < 0

# Argent total dépensé en moyenne par semaine

# TO DO
