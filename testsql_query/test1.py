import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "Betul3146")  # in industries we donot need set local host admin will give us url and pass
print(mydb) # just checking for connection
cursor = mydb.cursor()
#cursor.execute(("create database amit"))
cursor.execute("show databases")
print(cursor.fetchall())
#table = ("create table amit.myfamily(srn int(6) , name varchar(30) , age int(3) , occupation varchar(40) , mobile int(20))")

#q1 = cursor.execute(table)
#q2 = cursor.execute("select * from amit.myfamily")
#print(q2)




