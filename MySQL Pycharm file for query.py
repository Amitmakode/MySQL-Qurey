"built connection between python and mysql"
import mysql.connector as conn

mydb = conn.connect(host='localhost', user= 'root', password= 'Betul3146', database= 'practice_data')
cursor= mydb.cursor()

"create database if require or connect for exists database"
#cursor.execute("create database if not exists practice_data")

#cursor.execute("show databases")
#print(cursor.fetchall())


"create table in existing database"
#cursor.execute('create table if not exists practice_data.table2(name varchar(20), number int(12), email varchar(15))')
#cursor.execute("create table if not exists practice_data.table1(name varchar(20), number int(10), address varchar(50))")
#cursor.execute("create table if not exists practice_data.table3(name varchar(20), number int(12), education varchar(20))")

#cursor.execute("show tables")
#print(cursor.fetchall())

#table= cursor.execute('select * from practice_data.table3')
#for i in cursor.fetchall():
    #print(i)

"insert data values in tables by query"
#cursor.execute("insert into practice_data.table1 values('amit', 81818181, 'betul badora mp')")
#cursor.execute("insert into practice_data.table2 values('amit', 91919191, 'amit@gmail.com')")
#cursor.execute("insert into practice_data.table3 values('am', 71717767, 'mech engg')")
#mydb.commit()


"Another way to insert data"
#sql = "INSERT INTO table3 (name, number,education) VALUES (%s, %s, %s)"
#val = ("Ram", 3985479, "ajay nagar")
#cursor.execute(sql, val)
#mydb.commit()
#mydb.close()


"""create one more table in practice_data"""
#table = ("create table if not exists practice_data.bank_details( age int(20),job varchar(30),marital varchar(30),education varchar(30),`default` varchar(30),balance int,housing varchar(30),loan varchar(30),contact varchar(30),`day` int,`month` varchar(30),duration int,campaign int,pdays int,previous int,poutcome varchar(30),y varchar(30))")
#cursor.execute(table)


"""value = [(44, "technician", "single", "secondary", "no", 29, "yes", "no", "unknown", 5, "may", 151, 1,

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
(50, "management", "married", "secondary", "no", 49, "yes", "no", "unknown", 5, "may", 180, 2, -1, 0, "unknown", "no")]"""

#insert = "insert into bank_details(age,job,marital,education,`default`,balance,housing,loan,contact,`day`,`month`,duration,campaign,pdays,previous,poutcome,y) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#cursor.executemany(insert, value)
#mydb.commit()

#cursor.execute("select * from bank_details")
#cursor.fetchall()

#cursor.execute("select age, job,`default` from bank_details")

#cursor.execute("select * from bank_details where age = 41")

#cursor.execute("select job from bank_details where age = 41")

#cursor.execute("select * from bank_details where job = 'retired' and balance >100")

#cursor.execute("select * from bank_details where education = 'primary' or balance < 100")

#cursor.execute("select * from bank_details where education = 'primary' and balance < 100")

#cursor.execute("select distinct job from bank_details") #unique from list

#cursor.execute("select * from bank_details order by age")

#cursor.execute("select * from bank_details order by age desc")

#cursor.execute("select count(*) from bank_details")

#cursor.execute("select sum(balance) from bank_details")

#cursor.execute("select avg(balance) from bank_details")

#cursor.execute("select avg(age) from bank_details")

#cursor.execute("select min(balance) from bank_details")

#cursor.execute("select min(balance) from bank_details")

#cursor.execute("select max(balance) from bank_details")

#cursor.execute("select * from bank_details where balance = (select min(balance) from bank_details)")

#cursor.execute("select count(*) from bank_details group by marital")

#cursor.execute("select marital, count(*) from bank_details group by marital")

#cursor.execute("select marital, count(*), sum(balance) from bank_details group by marital")

#cursor.execute("select marital, count(*), sum(balance), avg(balance) from bank_details group by marital")

#cursor.execute("select marital, count(*), sum(balance), avg(balance) from bank_details group by marital having sum(balance)> 300")

#cursor.execute("set sql_safe_updates = 0")

#cursor.execute("update bank_details set balance = 0 where job = 'unknown'")

#cursor.execute("update bank_details set contact = 'known', y = 'yes' where month = 'may'")

#cursor.execute("update bank_details set `default` = 'null' where `default` = 'no'")

#cursor.execute("delete from bank_details where job = 'unknown'")

#cursor.execute("delete from bank_details where job = 'unknown'")

#cursor.execute("select * from (select job, age, education, y from bank_details ) as a where a.age = 58")


"""for create a shorted view from existing table"""
#cursor.execute("create view bank_view as select job, age, education, y from bank_details")

#cursor.execute("select * from bank_view where age = 58 bank_view")

"""cursor.execute("create table if not exists bank_details2\
(age int,job varchar(30),marital varchar(30),education varchar(30),`default` varchar(30),\
balance int,housing varchar(30),loan varchar(30),contact varchar(30),`day` int,`month` varchar(30),\
duration int,campaign int,pdays int,previous int,poutcome varchar(30),y varchar(30))")
"""

#cursor.execute("insert into practice_data.bank_details2 select * from bank_details")

#cursor.execute("select * from bank_details2")

#cursor.execute("insert into bank_details2 select * from bank_details where age = 58;")

#cursor.execute("select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details inner join bank_details2 on bank_details.age = bank_details2.age")

#cursor.execute("select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details right join bank_details2 on bank_details.age = bank_details2.age")

#cursor.execute("select bank_details.age, bank_details.job, bank_details.marital, bank_details.contact from bank_details left join bank_details2 on bank_details.age = bank_details2.age")

#cursor.execute("Drop table bank_details2")


"""for i in cursor.fetchall():
    print(i)"""

