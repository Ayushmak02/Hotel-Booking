#MAIN MODULE - MAIN MENU
import mysql.connector
import Room
import Hall
import Client
import Employee
print("\t\t\t\tHOTEL SAN")
print('''Welcome to HOTEL SAN.
Please select from the following:''')
print("======================================================================================")
z=1
while z==1:
    print()
    print("""1.Room Booking
2.Hall Booking
3.Alter Bookings
4.Client
5.Employee
6.Room
7.Hall
8.About us
9.Exit
  """)
    c=int(input("Enter your choice: "))
    print()
    import Room
    import Hall
    if c==1:
        Room.Book()
    if c==2:
        Hall.Book()
    if c==3:
        print("""1.Alter Room Booking
2.Alter Hall Booking""")
        w=int(input("Enter your choice: "))
        if w==1:
            Room.Change()
        elif w==2:
            Hall.Change()
        else:
            print("wrong choice")
    if c==4:
        print("""1.Show client details
2.Show specific client details
3.Alter client details
4.Delete client details""")
        q=int(input("Enter your choice: "))
        if q==1:
            Client.Showall()
        elif q==2:
            Client.Show()
        elif q==3:
            Client.Change()
        elif q==4:
            Client.Remove()
        else:
            print("wrong choice")
    if c==5:
        print("""1.Show Employee details
2.Show specific Employee details
3.Add Employee
4.Alter Employee details
5.Delete Employee details""")
        q=int(input("Enter your choice:"))
        if q==1:
            Employee.Showall()
        elif q==2:
            Employee.Show()
        elif q==3:
            Employee.Add()
        elif q==4:
            Employee.Change()
        elif q==5:
            Employee.Remove()
        else:
            print("wrong choice")
    if c==6:
        print("""1. Show all rooms
2. Show specific room
3. Delete room""")
        q=int(input("Enter your choice: "))
        if   q==1:
            Room.Showall()
        elif q==2:
            Room.Show()
        elif q==3:
            Room.Remove()
        else:
            print("wrong choice")
    if c==7:
        print("""1. Show all Halls
2. Show specific Hall
3. Delete Hall""")
        q=int(input("Enter your choice :"))
        if q==1:
            Hall.Showall()
        elif q==2:
            Hall.Show()
        elif q==3:
            Hall.Remove()
        else:
            print("wrong choice")
    if c==8:
        print("************** ABOUT US **************")
        print("""The four-star Hotel SAN is a jewel of the Modern architecture,
located in the strict centre of Delhi. Because of our prestigious location,
we have already  been a perfect place both for tourists, as well as business purposes.

We have comfortably equipped rooms, including many halls,
with over one hundred metres of surface area, which are sure to awe
even the most demanding Guests.
We offer 7 rooms, where we have been preparing family and business
meetings already for years.

Hotel SAN is not merely the building but, above all, its people.
We are a team of professionals, who can organise every event end-to-end.

We have many years of experience, extensive conference facilities,
as well as technical and catering equipment, and we will be more than happy to organise
your meeting – both in our building, in a tent at the hotel's patio,
as well as in any other place of your choosing.

WE ORGANISE:

wedding receptions,
first communion parties,
baptisms,
name-day parties,
funeral receptions,
prom,
mid-school balls,
graduate balls,
bachelorette and bachelor parties,
celebrations of defending a thesis,
conferences,
trainings,
galas,
business breakfasts,
company anniversary parties,
integration events and many others happy and cheerful events worth remembering.""")
    if c==9:
        print("EXITING!!!!!")
        break
    else:
        print()
        z=int(input("Enter 1 to start the system again, else press 0(zero) to end: "))
        if z==1:
            continue
        elif z==0:
            print("\t---------THANK YOU-----------")
            break
    
    

