import mysql.connector
import re

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="users")

cur=db.cursor()

def isvalid(h):
    p= re.compile('(^([+]{1}[8]{2})?(01){1}[1-9]{1}\d{8})$')
    return p.match(h)

print("Select 1 for changing Name or 2 for Phone Number")

z=input("Enter the digit (1 or 2):\n")

if z=='1':
    name= input("Enter the old Name:\n")

    if name=="":
        print("Please give information")

    else:
        m = (name,)

        k = 'SELECT name FROM phonebook WHERE name=%s'

        cur.execute(k, m)
        result = cur.fetchall()

        if not result:
            print("Not found. Please put the correct Name....")

        else:
            q = input("Enter the new Name:\n")
            a = 'UPDATE phonebook set name=%s WHERE name=%s'

            cur.execute(a, (q, name))
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

elif z=='2':

    phonenumber= input("Enter the Phone Number to be Updated:\n")

    try:
        if phonenumber == "":
            print("Please give information")

        else:
            n = (phonenumber,)

            o = 'SELECT name FROM phonebook WHERE phonenumber=%s'

            cur.execute(o, n)
            e = cur.fetchall()

            if not e:
                print("Not found. Please put the correct Phone Number....")

            else:
                h = input("Enter the new Phone Number:\n")

                j = len(h)

                if j >= 11 and j<=14:
                    if isvalid(h):
                        b = 'UPDATE phonebook set phonenumber=%s WHERE phonenumber=%s'

                        cur.execute(b, (h, phonenumber))
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

else:
    print("Wrong digit. Try again....")