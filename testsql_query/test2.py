import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "Betul3146")  # in industries we donot need set local host admin will give us url and pass

cursor = mydb.cursor()

cursor.execute("insert into amit.myfamily values(01, 'mom', 59, 'house wife', 986899889)")
cursor.execute("insert into amit.myfamily values(01, 'mom', 59, 'house wife', 986899889)")
cursor.execute("insert into amit.myfamily values(01, 'mom', 59, 'house wife', 986899889)")
cursor.execute("insert into amit.myfamily values(01, 'mom', 59, 'house wife', 986899889)")
mydb.commit()
cursor.execute("select * from amit.myfamily")
for i in cursor.fetchall():
    print(i)