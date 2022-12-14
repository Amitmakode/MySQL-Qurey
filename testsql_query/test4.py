show databases

create database datascience
use datascience
create table if not exists bank_details(
age int,
job varchar(30),
marital varchar(30),
education varchar(30),
`default` varchar(30),
balance int,
housing varchar(30),
loan varchar(30),
contact varchar(30),
`day` int,
`month` varchar(30),
duration int,
campaign int,
pdays int,
previous int,
poutcome varchar(30),
y varchar(30))

show tables

Describe bank_details

insert into bank_details values(58, "management", "married", "tertiary", "no", 2143, "yes", "no", "unknown", 5, "may", 261, 1, -1, 0, "unknown",
       "no")

select * from bank_details

insert into bank_details values(44, "technician", "single", "secondary", "no", 29, "yes", "no", "unknown", 5, "may", 151, 1, -

1, 0, "unknown", "no"),
(33, "entrepreneur", "married", "secondary", "no", 2, "yes", "yes", "unknown", 5, "may", 76, 1, -1, 0, "unknown", "no"),
(47, "blue-collar", "married", "unknown", "no", 1506, "yes", "no", "unknown", 5, "may", 92, 1, -1, 0, "unknown", "no"),
(33, "unknown", "single", "unknown", "no", 1, "no", "no", "unknown", 5, "may", 198, 1, -1, 0, "unknown", "no"),
(35, "management", "married", "tertiary", "no", 231, "yes", "no", "unknown", 5, "may", 139, 1, -1, 0, "unknown", "no"),
(28, "management", "single", "tertiary", "no", 447, "yes", "yes", "unknown", 5, "may", 217, 1, -1, 0, "unknown", "no"),
(
42, "entrepreneur", "divorced", "tertiary", "yes", 2, "yes", "no", "unknown", 5, "may", 380, 1, -1, 0, "unknown", "no"),
(58, "retired", "married", "primary", "no", 121, "yes", "no", "unknown", 5, "may", 50, 1, -1, 0, "unknown", "no"),
(43, "technician", "single", "secondary", "no", 593, "yes", "no", "unknown", 5, "may", 55, 1, -1, 0, "unknown", "no"),
(41, "admin.", "divorced", "secondary", "no", 270, "yes", "no", "unknown", 5, "may", 222, 1, -1, 0, "unknown", "no"),
(29, "admin.", "single", "secondary", "no", 390, "yes", "no", "unknown", 5, "may", 137, 1, -1, 0, "unknown", "no"),
(53, "technician", "married", "secondary", "no", 6, "yes", "no", "unknown", 5, "may", 517, 1, -1, 0, "unknown", "no"),
(58, "technician", "married", "unknown", "no", 71, "yes", "no", "unknown", 5, "may", 71, 1, -1, 0, "unknown", "no"),
(57, "services", "married", "secondary", "no", 162, "yes", "no", "unknown", 5, "may", 174, 1, -1, 0, "unknown", "no"),
(51, "retired", "married", "primary", "no", 229, "yes", "no", "unknown", 5, "may", 353, 1, -1, 0, "unknown", "no"),
(45, "admin.", "single", "unknown", "no", 13, "yes", "no", "unknown", 5, "may", 98, 1, -1, 0, "unknown", "no"),
(57, "blue-collar", "married", "primary", "no", 52, "yes", "no", "unknown", 5, "may", 38, 1, -1, 0, "unknown", "no"),
(60, "retired", "married", "primary", "no", 60, "yes", "no", "unknown", 5, "may", 219, 1, -1, 0, "unknown", "no"),
(33, "services", "married", "secondary", "no", 0, "yes", "no", "unknown", 5, "may", 54, 1, -1, 0, "unknown", "no"),
(28, "blue-collar", "married", "secondary", "no", 723, "yes", "yes", "unknown", 5, "may", 262, 1, -1, 0, "unknown",
 "no"),
(56, "management", "married", "tertiary", "no", 779, "yes", "no", "unknown", 5, "may", 164, 1, -1, 0, "unknown", "no"),
(32, "blue-collar", "single", "primary", "no", 23, "yes", "yes", "unknown", 5, "may", 160, 1, -1, 0, "unknown", "no"),
(25, "services", "married", "secondary", "no", 50, "yes", "no", "unknown", 5, "may", 342, 1, -1, 0, "unknown", "no"),
(40, "retired", "married", "primary", "no", 0, "yes", "yes", "unknown", 5, "may", 181, 1, -1, 0, "unknown", "no"),
(44, "admin.", "married", "secondary", "no", -372, "yes", "no", "unknown", 5, "may", 172, 1, -1, 0, "unknown", "no"),
(39, "management", "single", "tertiary", "no", 255, "yes", "no", "unknown", 5, "may", 296, 1, -1, 0, "unknown", "no"),
(52, "entrepreneur", "married", "secondary", "no", 113, "yes", "yes", "unknown", 5, "may", 127, 1, -1, 0, "unknown",
 "no"),
(46, "management", "single", "secondary", "no", -246, "yes", "no", "unknown", 5, "may", 255, 2, -1, 0, "unknown", "no"),
(36, "technician", "single", "secondary", "no", 265, "yes", "yes", "unknown", 5, "may", 348, 1, -1, 0, "unknown", "no"),
(57, "technician", "married", "secondary", "no", 839, "no", "yes", "unknown", 5, "may", 225, 1, -1, 0, "unknown", "no"),
(49, "management", "married", "tertiary", "no", 378, "yes", "no", "unknown", 5, "may", 230, 1, -1, 0, "unknown", "no"),
(60, "admin.", "married", "secondary", "no", 39, "yes", "yes", "unknown", 5, "may", 208, 1, -1, 0, "unknown", "no"),
(59, "blue-collar", "married", "secondary", "no", 0, "yes", "no", "unknown", 5, "may", 226, 1, -1, 0, "unknown", "no"),
(
51, "management", "married", "tertiary", "no", 10635, "yes", "no", "unknown", 5, "may", 336, 1, -1, 0, "unknown", "no"),
(57, "technician", "divorced", "secondary", "no", 63, "yes", "no", "unknown", 5, "may", 242, 1, -1, 0, "unknown", "no"),
(25, "blue-collar", "married", "secondary", "no", -7, "yes", "no", "unknown", 5, "may", 365, 1, -1, 0, "unknown", "no"),
(53, "technician", "married", "secondary", "no", -3, "no", "no", "unknown", 5, "may", 1666, 1, -1, 0, "unknown", "no"),
(36, "admin.", "divorced", "secondary", "no", 506, "yes", "no", "unknown", 5, "may", 577, 1, -1, 0, "unknown", "no"),
(37, "admin.", "single", "secondary", "no", 0, "yes", "no", "unknown", 5, "may", 137, 1, -1, 0, "unknown", "no"),
(44, "services", "divorced", "secondary", "no", 2586, "yes", "no", "unknown", 5, "may", 160, 1, -1, 0, "unknown", "no"),
(50, "management", "married", "secondary", "no", 49, "yes", "no", "unknown", 5, "may", 180, 2, -1, 0, "unknown", "no")

select * from bank_details

select age, job, `default` from bank_details

select * from bank_details where age = 41

select job from bank_details where age = 41
select * from bank_details where job = 'retired' and balance > 100

select * from bank_details where education = 'primary' or balance < 100

select * from bank_details where

education = 'primary' and balance < 100

select distinct job from bank_details

select * from bank_details order by age

select * from bank_details order by age desc

select count(*) from bank_details

select sum(balance) from bank_details

selectavg(balance) from bank_details

select avg(age) from bank_details

select min(balance) from bank_details

select max(balance) from bank_details

select * from bank_details where balance = (select min(balance) from bank_details)

select count(*) from bank_details group by marital
select marital, count(*) from bank_details group by marital
select marital, count(*), sum(balance) from bank_details group by marital
select marital, count(*), sum(balance), avg(balance) from bank_details group by marital
select marital, count(*), sum(balance), avg(balance) from bank_details group by marital having sum(balance) > 300

set sql_safe_updates = 0
update bank_details set balance = 0 where job = 'unknown'

update bank_details set contact = 'known', y = 'yes' where month = 'may'

update bank_details set `default` = 'null' where `default` = 'no'

delete from bank_details where job = 'unknown'

select * from bank_details

DELIMITER &&
create procedure select_filter()
BEGIN
   select * from bank_details;
END &&

call select_filter()

DELIMITER &&
create procedure select_filter_avg()
BEGIN
    selectavg(balance) from bank_details;
END &&

call select_filter_avg()

DELIMITER &&
create procedure select_filter1(IN var int)
BEGIN
   select * from bank_details where job = 'retired' and balance > var;
END &&

call select_filter1(150)

DELIMITER &&
create procedure select_filter2(IN var int, IN var1 varchar(30))
BEGIN
   select * from bank_details where job = var1 and balance > var;
END &&

call select_filter2(100, 'services')

select * from (select job, age, education, y from bank_details) as a where a.age = 58

create view bank_view as select job, age, education, y from bank_details

select * from bank_view where age = 58 bank_view

create table if not exists bank_details2(
age int,
job varchar(30),
marital
varchar(30),
education
varchar(30),
`default`
varchar(30),
balance
int,
housing
varchar(30),
loan
varchar(30),
contact
varchar(30),
`day`
int,
`month`
varchar(30),
duration
int,
campaign
int,
pdays
int,
previous
int,
poutcome
varchar(30),
y
varchar(30))

insert into bank_details_copy select * from bank_details
select * from bank_details_copy
insert into bank_details2 select * from bank_details where age = 58;

select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details inner join bank_details2 on bank_details.age = bank_details2.age

select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details right join bank_details2 on bank_details.age = bank_details2.age

select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details left join bank_details2 on bank_details.age = bank_details2.age

Drop table bank_details_copy

show tables
