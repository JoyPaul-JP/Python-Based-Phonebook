import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="users")

cur=db.cursor()

print("Select 1 for Deleting information by Name or 2 for by Phone Number")

z=input("Enter the digit (1 or 2):\n")

if z=='1':
    name= input("Enter the Name:\n")

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

elif z=='2':

    phonenumber= input("Enter the Phone Number:\n")

    if phonenumber=="":
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