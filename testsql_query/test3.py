import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "Betul3146")  # in industries we donot need set local host admin will give us url and pass

cursor = mydb.cursor()

cursor.execute("select name, age, srn from amit.myfamily")
#for i in cursor.fetchall():
    #print(i)

"""l =[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))"""

print(cursor.fetchall())
