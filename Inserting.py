import mysql.connector
import re

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="users")

cur=db.cursor()

def isvalid(r):
    p= re.compile('(^([+]{1}[8]{2})?(01){1}[1-9]{1}\d{8})$')
    return p.match(r)

q= input("Enter Name:\n")

if q=="":
    print("Please give information")

else:
    r = input("Enter Phone Number:\n")

    try:
        if r == "":
            print("Please give information")
        else:
            j = len(r)

            if j >= 11 and j<=14:
                if isvalid(r):
                    a = 'INSERT INTO phonebook values(%s,%s)'

                    b = (q, r)

                    cur.execute(a, b)
                    db.commit()

                    print("The updated PhoneBook is:\n")
                    f = 'select * from phonebook'

                    cur.execute(f)
                    t = cur.fetchall()
                    t.sort()

                    for item in t:
                        for subitem in item:
                            print(str(subitem).center(10), end='')
                        print()

                else:
                    print("Invalid mobile number. Please give the correct mobile number")

            else:
                print("Invalid mobile number. Please give the correct mobile number")

    except Exception as s:
        print("This value is already existed. Try another value.")


