select name, god from albomi
where god = 2018;

select name, duration from trek
 order by duration desc
 limit 1;
select name, duration from trek
where duration>=3.5;
select names, god from sbornik
where god between 2018 and 2020;

select name from ispolniteli
where name not like '%% %%';

select name from trek
where name like '%%my%%';







