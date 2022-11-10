create table if not exists mainmenu(
id integer primary autoincrement,
title text not null,
url text not null
)

create table if not exists recepts(
id integer primary key autoincrement,
title text not null,
recept text not null,
url text not null)