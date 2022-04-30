delete from ganri;

insert into ganri(id, name)
values
	(1, 'rock'),
	(2, 'pop'),
	(3, 'jazz'),
	(4, 'classic'),
	(5, 'folk');

delete from ispolniteli;

insert into ispolniteli(id,name,surname,psevdonim)
values
    (1,'misha mik','petrov','mixarock'),
    (2,'sasha','ivanov','sashapop'),
    (3,'masha','sidorova','maxajazz'),
    (4,'vova','kozlov','vovaclass'),
    (5,'daria','pirogova','daxafolk'),
    (6,'lena','kirilova','lenarock'),
    (7,'vitia','pechkin','vitokfolk'),
    (8,'luba','vesenina','lubaclass');
 
   
delete from albomi;

insert into albomi(id,name,god)
values 
     (1,'mishaalbom', 2017),
     (2,'sashaalbom',2018),
     (3,'mashaalbom',2019),
     (4,'vovaalbom',2020),
     (5,'dariaalbom',2021),
     (6,'lenaalbom',2018),
     (7,'vitiaalbom',2019),
     (8,'lubaalbom',2020);
    
 insert into trek(id,id_albomi,name,duration)
 values 
     (1,1,'mymisha',3.3),
     (2,2,'mysasha', 3.5),
     (3,2,'yoursaha', 2.5),
     (4,3,'mymasha', 3.7),
     (5,3,'yourmasha', 2.4),
     (6,4,'myvova', 4.5),
     (7,4,'yourvova', 1.5),
     (8,5,'mydaria', 4.7),
     (9,5,'yourdaria', 2.9),
     (10,6,'mylena', 3.8),
     (11,6,'yourlena', 2.4),
     (12,7,'myvitia', 3.3),
     (13,7,'yourvitia', 2.8),
     (14,8,'myluba', 4.1),
     (15,8,'yourluba', 2.7);
    
 insert into sbornik(id,names,god)
 values
      (1,'sbornikmisha',2018),
      (2,'sborniksash',2017),
      (3,'sbornikmasha',2019),
      (4,'sbornikvova',2020),
      (5,'sbornikdaria',2021),
      (6,'sborniklena',2019),
      (7,'sbornikvitia',2020),
      (8,'sbornikluba',2018);
     
   delete from ganri_idispolniteli  
     
  insert into ganri_idispolniteli(id_ganri,id_ispolniteli)
  values 
      (1,1),
      (2,2),
      (3,3),
      (4,4),
      (5,5),
      (1,6),
      (5,7),
      (4,8);
     
 insert into ispolniteli_albomi(id_ispolniteli, id_albomi)
 values 
     (1,1),
     (2,2),
     (3,3),
     (4,4),
     (5,5),
     (6,6),
     (7,7),
     (8,8);
 insert into trek_sbornik(id_trek, Id_sbornik)
 values 
     (1,1),
     (2,2),
     (3,2),
     (4,3),
     (5,3),
     (6,4),
     (7,4),
     (8,5),
     (9,5),
     (10,6),
     (11,6),
     (12,7),
     (13,7),
     (14,8),
     (15,8);
    
    
    
    
    
    
     
      
     
    
    
   
   
   
   
    