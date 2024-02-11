import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='mysql',database="users")

cur=db.cursor()

def main():
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

    repeat = input("Enter the digit: \n").lower()
    if repeat == "1":
        main()
    elif repeat == "2":
        print("Thanks for visiting...")
        exit()
    else:
        print("Wrong digit. Thanks for visiting. Try again...")

main()
