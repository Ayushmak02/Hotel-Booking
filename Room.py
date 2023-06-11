#PYTHON MODULE : ROOM
import mysql.connector
def Book():
    #FUNCTION TO BOOK A ROOM
    choice=1
    while choice==1:
        try:
            print("******************* ROOM BOOKING *******************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter room number: "))
            name=input("Enter client name: ")
            num=int(input("Enter client's Phone Number: "))
            ad=int(input("Enter client's aadhar Number: "))
            em=input("Enter client's email address: ")
            addr=input("Enter residence: ")
            noadult=int(input("Enter total no. of adults: "))
            nochild=int(input("Enter total no. of children: "))
            print("\tList of ecodes :")
            cur.execute("select ecode from employee")
            for a in cur:
                print("\t",a)
            ecode=int(input("Enter designated employee's code from above: "))
            print("1. Delux ")
            print("2. Classic")
            print("3. Premium")
            print("4. Gold")
            x=int(input("Enter the type of room(serial no.) :  "))
            if   x==1:
                typ="Delux"
            elif x==2:
                typ="Classic"
            elif x==3:
                typ="Premium"
            elif x==4:
                typ="Gold"
            hallno=0
            h=int(input("Enter number of days of stay: "))
            if   x==1:
                      rent=15000
            elif x==2:
                      rent=8000
            elif x==3:
                      rent=10000
            elif x==4:
                      rent=13500
            trent=h*rent
            print("TOTAL AMOUNT = Rs.",trent)
            t=(name,num,ad,em,addr,noadult,nochild,n,hallno)
            g=("insert into custom values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            cur.execute(g,t)
            i=(n,ad,typ,ecode,rent,trent,h)
            f=("insert into room values(%s,%s,%s,%s,%s,%s,%s)")
            cur.execute(f,i)
            db.commit()
            print("\t~~~~~~~~~~~~~~~~~~~HOTEL SAN~~~~~~~~~~~~~~~~~~")
            print("\t-------------------RECEIPT------------------")
            print("\tNAME: ",name)
            print("\tROOM NUMBER: ",n)
            print("\tPHONE NUMBER: ",num)
            print("\tNUMBER OF DAYS OF STAY: ",h)
            print("\tTOTAL AMOUNT: Rs.",trent)
            print("-----------------------------------------------")
            qn=("select ename,eno,eemail from room,employee where room.ecode=employee.ecode and roomno=%s")
            mn=(n,)
            cur.execute(qn,mn)
            for a,b,c in cur:
                print("\t\tEMPLOYEE DETAILS:")
                print("\t\tNAME: ",a)
                print("\t\tEMPLOYEE CODE: ",ecode)
                print("\t\tNUMBER: ",b)
                print("\t\tE MAIL: ",c)
            print("-----------------------------------------------")
            print("##############THANK YOU ####################")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue booking?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("ROOMS BOOKED")

def Change():
    #FUNCTION TO CHANGE TO BOOKINGS OF A ROOM
    choice=1
    while choice==1:
        try:
            print()
            print("*******************CHANGE ROOM BOOKING*******************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            x=int(input("Enter the room number where changes are to be done: "))
            b=(x,)
            print('''Select from the following (where the change has to be done)
    1.Name
    2.Phone number
    3.Email-ID
    4.No. of days of stay
    5.Adhaar Number
    6.Address
    7.No. of adults
    8.No. of children
    9.Type of room''')
            y=int(input("Enter your choice: "))
            if y==1:
                l=("select clname from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original name= ",d)
                p=input("Enter new name: ")
                q=("update custom set clname=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==2:
                l=("select clno from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original number= ",d)
                p=int(input("Enter new number: "))
                q=("update custom set clno=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==3:
                l=("select clemail from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original email= ",d)
                p=input("Enter new Email-ID: ")
                q=("update custom set clemail=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==4:
                a=("select roomtypr from room where roomno=%s")
                cur.execute(a,b)
                c=cur.fetchone()
                for d in c:
                    print("Room type: ",d)
                if   d=="Delux":
                      rent=15000
                elif d=="Classic":
                      rent=8000
                elif d=="Premium":
                      rent=10000
                elif d=="Gold":
                      rent=13500
                l=("select days from room where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of days= ",d)
                p=int(input("Enter new number of days of stay: "))
                trent=p*rent
                print("TOTAL AMOUNT = Rs.",trent)
                q=("update room set days=%s,roomrent=%s,total=%s where roomno=%s")
                t=(p,rent,trent,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==5:
                l=("select claadhar from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original adhaar no.= ",d)
                p=int(input("Enter new Adhaar no.: "))
                q=("update custom set claadhar=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                q=("update room set cusadhaar=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==6:
                l=("select address from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original address= ",d)
                p=input("Enter new Address: ")
                q=("update custom set address=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==7:
                l=("select noofadul from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of adults= ",d)
                p=int(input("Enter new No. of Adults (new): "))
                q=("update custom set noofadul=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==8:
                l=("select noofchildren from custom where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of children= ",d)
                p=int(input("Enter new No. of Children (new): "))
                q=("update custom set noofchildren=%s where roomno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==9:
                l=("select roomtypr from room where roomno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original room type= ",d)
                print()
                print("1. Delux ")
                print("2. Classic")
                print("3. Premium")
                print("4. Gold")
                n=int(input("Enter the type of room(serial no.) :  "))
                if    n==1:
                    typ="Delux"
                elif  n==2:
                    typ="Classic"
                elif  n==3:
                    typ="Premium"
                elif  n==4:
                    typ="Gold"
                if    n==1:
                      rent=15000
                elif  n==2:
                      rent=8000
                elif  n==3:
                      rent=10000
                elif  n==4:
                      rent=13500
                h=int(input("Enter no. of days of stay: "))
                trent=h*rent
                print("TOTAL AMOUNT = Rs.",trent)
                q=("update room set roomtypr=%s,roomrent=%s,total=%s,days=%s where roomno=%s")
                t=(typ,rent,trent,h,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue changing details?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("CHANGES DONE!")


def Showall():
    #FUNCTION TO SHOW DETAILS OF ALL ROOMS
    try:
        db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
        cur=db.cursor()
        print("***********************DETAILS OF ALL ROOMS***********************")
        q=("Select * from room")
        cur.execute(q)
        for (a,b,c,d,e,f,g) in cur:
            print()
            print("\tRoom number: ",a)
            print("\tCustomer's Adhaar no. : ",b)
            print("\tRoom type: ",c)
            print("\tEmployee's code: ",d)
            print("\tRoom rent: ",e)
            print("\tTotal rent: ",f)
            print("\tNo. of days of stay: ",g)
            print()
    except:
        print("ERROR!!!!! PLEASE TRY AGAIN....")

def Show():
    # FUNCTION TO SHOW DETAILS OF A SPECIFIC ROOM
    choice=1
    while choice==1:
        try:
            print("***********************DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the room number: "))
            q=("select * from room where roomno= %s")
            v=(n,)
            cur.execute(q,v)
            for (a,b,c,d,e,f,g) in cur:
                print()
                print("\tRoom number: ",a)
                print("\tCustomer's Adhaar no. : ",b)
                print("\tRoom type: ",c)
                print("\tEmployee's code: ",d)
                print("\tRoom rent: ",e)
                print("\tTotal rent: ",f)
                print("\tNo. of days of stay: ",g)
                print()
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue viewing details?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print()

def Remove():
    # FUNCTION TO DELETE A ROOM
    choice=1
    while choice==1:
        try:
            print("***********************REMOVE ROOM DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the room number: "))
            q=("delete from room where roomno=%s")
            v=(n,)
            cur.execute(q,v)
            db.commit()
            print("           ROOM REMOVED!!!!")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue removing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("ROOMS DELETED!")
