-- Usage : 
-- "sqlite3 dev.sqlite3 < products.sql"

delete from products;

-- id, name, price, color, asso_price
-- /!\ les prix sont en int : 1.50€ -> 150     2.00€ -> 200      0.60€ -> 60

insert into products values (1, "Boisson", null, "#f6e58d", 60);
insert into products values (2, "Twix", null, "#55efc4", 40);
insert into products values (3, "Bueno", null, "#c7ecee", 70);
insert into products values (4, "Smarties", null, "#686de0", 60);
insert into products values (5, "PastaBox", null, "#fab1a0", 220);
insert into products values (6, "Riz", null, "#c7ecee", 170);
insert into products values (7, "Sandwich", null, "#c7ecee", 170);
insert into products values (8, "Cafés", null, "#778beb", 40);
insert into products values (9, "Lion", null, "#ffbe76", 40);
insert into products values (10, "Gauffre Sucre", null, "#ffbe76", 40);
insert into products values (11, "Gauffre Choco", null, "#e17055", 50);
insert into products values (12, "Bounty", null, "#81ecec", 50);
insert into products values (13, "Snickers", null, "#e17055", 50);
insert into products values (14, "Monster", null, "#cf6a87", 120);
insert into products values (15, "PomPote", null, "#55efc4", 40);
insert into products values (16, "Bready", null, "#c7ecee", 70);
insert into products values (17, "Nestle", null, "#f9ca24", 60);
insert into products values (18, "Crunch", null, "#a29bfe", 60);
insert into products values (19, "KitKat", null, "#a3cbae", 60);
insert into products values (20, "M&Ms", null, "#a29bfe", 60);
insert into products values (21, "Dragibus", null, "#820ecec", 50);
insert into products values (22, "Caprisun", null, "#ffeaa7", 30);
insert into products values (23, "PastaXtrem", null, "#f5cd79", 370);
insert into products values (24, "Nouilles", null, "#ea8685", 110);
insert into products values (25, "Chips", null, "#c7ecee", 70);