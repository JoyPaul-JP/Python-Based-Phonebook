import mysql.connector
import re

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="users")

cur=db.cursor()

f= 'select * from phonebook'

cur.execute(f)
t = cur.fetchall()
t.sort()

for item in t:
    for subitem in item:
        print(str(subitem).center(10), end='')
    print()
