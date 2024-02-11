import mysql.connector
import re

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="own")

cur=db.cursor()

print("Hello, Welcome to this website.")
input("Press Enter button to Continue.....\n")

print("This is your PhoneBook\n")

f= 'select * from phonebook'

cur.execute(f)
t = cur.fetchall()
t.sort()

for item in t:
    for subitem in item:
        print(str(subitem).center(15), end='')
    print()

print("\n")

print("If you want to perform any action,")
input("Press Enter button to Continue.....\n")


def main():

    print("Please choose: \n Select 1 for Inserting data,\n Select 2 for Searching data,\nSelect 3 for Updating data,\nSelect 4 for Deleting data\n")
    z = input("Enter the digit (1 or 2 or 3 or 4):\n")

    if z == '1':

        def isvalid(r):
            p = re.compile('(^([+]{1}[8]{2})?(01){1}[1-9]{1}\d{8})$')
            return p.match(r)

        q = input("Enter Name:\n")

        if q == "":
            print("Please give information")

        else:
            r = input("Enter Phone Number:\n")

            try:
                if r == "":
                    print("Please give information")
                else:
                    j = len(r)

                    if j >= 11 and j <= 14:
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

    elif z == '2':
        print("Select 1 for searching by Name or 2 for Phone Number")

        z = input("Enter the digit (1 or 2):\n")

        if z == '1':
            name = input("Enter the Name for searching:\n")
            if name == "":
                print("Please give information")

            else:
                m = (name,)

                a = 'SELECT * FROM phonebook WHERE name=%s'

                cur.execute(a, m)
                result = cur.fetchall()

                if not result:
                    print("Not found. Try again....")

                else:
                    print(result)


        elif z == '2':

            phonenumber = input("Enter the Phone Number for searching:\n")

            if phonenumber == "":
                print("Please give information")

            else:
                n = (phonenumber,)

                b = 'SELECT * FROM phonebook WHERE phonenumber=%s'

                cur.execute(b, n)
                result = cur.fetchall()

                if not result:
                    print("Not found. Try again....")

                else:
                    print(result)


        else:
            print("Wrong digit. Try again....")

    elif z == '3':

        def isvalid(h):
            p = re.compile('(^([+]{1}[8]{2})?(01){1}[1-9]{1}\d{8})$')
            return p.match(h)

        print("Select 1 for changing Name or 2 for Phone Number")

        z = input("Enter the digit (1 or 2):\n")

        if z == '1':
            name = input("Enter the old Name:\n")

            if name == "":
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

        elif z == '2':

            phonenumber = input("Enter the Phone Number to be Updated:\n")

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

                        if j >= 11 and j <= 14:
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

    elif z == '4':

        print("Select 1 for Deleting information by Name or 2 for by Phone Number")

        z = input("Enter the digit (1 or 2):\n")

        if z == '1':
            name = input("Enter the Name:\n")

            if name == "":
                print("Please give information")

            else:
                m = (name,)

                k = 'SELECT name FROM phonebook WHERE name=%s'

                cur.execute(k, m)
                result = cur.fetchall()

                if not result:
                    print("Not found. Please put the correct Name....")

                else:
                    a = 'DELETE FROM phonebook WHERE name=%s'

                    cur.execute(a, m)
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

        elif z == '2':

            phonenumber = input("Enter the Phone Number:\n")

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
                    b = 'DELETE FROM phonebook WHERE phonenumber=%s'

                    cur.execute(b, n)
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
            print("Wrong digit. Try again....")


    else:
        print("Wrong digit. Try again....")


    print("\nWould you like to run again?\n Select 1 for 'YES' and 2 for 'No'\n")
    repeat= input ("Enter the digit: \n").lower()
    if repeat == "1":
        main()
    elif repeat == "2":
        print("Thanks for visiting...")
        exit()
    else:
        print("Wrong digit. Thanks for visiting. Try again...")

main()
