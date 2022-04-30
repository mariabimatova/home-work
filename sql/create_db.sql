create table if not exists ispolniteli
(id serial  primary key, name varchar (15) not null , surname varchar (25) not null,
psevdonim varchar (25));

create table if not exists ganri
(id serial primary key, name varchar(15) not null);

create table if not exists ganri_idispolniteli  
(id_ganri  integer references ganri(id),
id_ispolniteli  integer  references ispolniteli (id),
constraint pk primary key (id_ganri, id_ispolniteli)); 

create table if not exists albomi
(id serial primary key, name varchar(40) not null, god integer);

create table if not exists ispolniteli_albomi  
(id_ispolniteli  integer  references ispolniteli (id),
id_albomi  integer  references albomi(id),
constraint pk1 primary key (id_albomi, id_ispolniteli));

create table if not exists trek
(id serial primary key, id_albomi  integer not null references albomi (id),
name varchar(40) not null, duration  numeric not null);

create table if not exists sbornik 
(id serial primary key, names varchar(40) not null, god integer not null);

create table if not exists trek_sbornik 
( id_trek integer references trek(id),
id_sbornik  integer references  sbornik (id),
constraint pk2 primary key (id_trek, id_sbornik));
