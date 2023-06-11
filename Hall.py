#PYTHON MODULE : EVENT
import mysql.connector
def Book():
    #FUNCTION TO BOOK A HALL
    choice=1
    while choice==1:
        try:
            print("******************* EVENT BOOKING *******************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter hall number: "))
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
            ecode=int(input("Enter designated employee's code: "))
            g=0
            print("1. Birthday ")
            print("2. Wedding/Anniversary")
            print("3. Get Together")
            print("4. Others")
            x=int(input("Enter the type of event(serial no.) :  "))
            if x==1:
                typ="Birthday"
            elif x==2:
                typ="Wedding/Anniversary"
            elif x==3:
                typ="Get Together"
            elif x==4:
                typ="Others"
            h=int(input("Enter number of days of event: "))
            if   x==1:
                      rent=15000
            elif x==2:
                      rent=50000
            elif x==3:
                      rent=20000
            elif  x==4:
                      rent=10000
            trent=h*rent
            print("TOTAL AMOUNT = Rs.",trent)
            t=(name,num,ad,em,addr,noadult,nochild,g,n)
            g=("insert into custom values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            cur.execute(g,t)
            i=(n,typ,ad,ecode,rent,trent,h)
            f=("insert into event values(%s,%s,%s,%s,%s,%s,%s)")
            cur.execute(f,i)
            db.commit()
            print("\t~~~~~~~~~~~~~~~~~~~HOTEL SAN~~~~~~~~~~~~~~~~~~")
            print("\t------------------RECEIPT------------------")
            print("\tNAME: ",name)
            print("\tHALL NUMBER: ",n)
            print("\tPHONE NUMBER: ",num)
            print("\tNUMBER OF DAYS OF EVENT: ",h)
            print("\tTOTAL AMOUNT: Rs.",trent)
            print("-----------------------------------------------")
            qn=("select ename,eno,eemail from event,employee where event.ecode=employee.ecode and hallno=%s")
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
        print("HALLS BOOKED")

def Change():
    #FUNCTION TO CHANGE TO BOOKINGS OF A HALL
    choice=1
    while choice==1:
        try:
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            print()
            print("*******************CHANGE HALL BOOKING*******************")
            x=int(input("Enter the hall number where changes are to be done: "))
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
    9.Type of event''')
            y=int(input("Enter your choice: "))
            if y==1:
                l=("select clname from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original name= ",d)
                p=input("Enter new name: ")
                q=("update custom set clname=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==2:
                l=("select clno from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original number= ",d)
                p=int(input("Enter new number: "))
                q=("update custom set clno=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==3:
                l=("select clemail from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original email= ",d)
                p=input("Enter new Email-ID: ")
                q=("update custom set clemail=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==4:
                a=("select event from event where hallno=%s")
                cur.execute(a,b)
                c=cur.fetchone()
                for d in c:
                    print("Event type: ",d)
                if d=="Birthday":
                    rent=15000
                elif d=="Wedding/Anniversary":
                    rent=50000
                elif d=="Get Together":
                    rent=20000
                elif d=="Others":
                    rent=10000
                l=("select days from event where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of days= ",d)
                p=int(input("Enter new number of days of stay: "))
                trent=p*rent
                print("TOTAL AMOUNT = Rs.",trent)
                q=("update event set days=%s,roomrent=%s,total=%s where hallno=%s")
                t=(p,rent,trent,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==5:
                l=("select claadhar from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original adhaar no.= ",d)
                p=int(input("Enter new Adhaar no.: "))
                q=("update custom set claadhar=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                q=("update event set cusadhaar=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==6:
                l=("select address from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original address= ",d)
                p=input("Enter new Address: ")
                q=("update custom set address=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            
            elif y==7:
                l=("select noofadul from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of adults= ",d)
                p=int(input("Enter new No. of Adults (new): "))
                q=("update custom set noofadul=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==8:
                l=("select noofchildren from custom where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of children= ",d)
                p=int(input("Enter new No. of Children (new): "))
                q=("update custom set noofchildren=%s where hallno=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==9:
                l=("select event from event where hallno=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original event type= ",d)
                print("1. Birthday ")
                print("2. Wedding/Anniversary")
                print("3. Get Together")
                print("4. Others")
                x=int(input("Enter the type of event(serial no.) :  "))
                if x==1:
                    typ="Birthday"
                elif x==2:
                    typ="Wedding/Anniversary"
                elif x==3:
                    typ="Get Together"
                elif x==4:
                    typ="Others"
                h=int(input("Enter number of days of event: "))
                if   h==1:
                      rent=15000
                elif h==2:
                      rent=50000
                elif h==3:
                      rent=20000
                elif  h==4:
                      rent=10000
                trent=h*rent
                print("TOTAL AMOUNT = Rs.",trent)
                q=("update event set event=%s,roomrent=%s,total=%s,days=%s where hallno=%s")
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
    #FUNCTION TO SHOW DETAILS OF ALL HALLS
    try:
        db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
        cur=db.cursor()
        print("***********************DETAILS OF ALL EVENTS***********************")
        q=("Select * from event")
        cur.execute(q)
        for (a,b,c,d,e,f,g) in cur:
            print()
            print("\tHall number: ",a)
            print("\tEvent type : ",b)
            print("\tCustomer's Adhaar no. : ",c)
            print("\tEmployee's code: ",d)
            print("\tHall rent: ",e)
            print("\tTotal rent: ",f)
            print("\tNo. of days of stay: ",g)
            print()
    except:
        print("ERROR!!!!! PLEASE TRY AGAIN....")

def Show():
    # FUNCTION TO SHOW DETAILS OF A SPECIFIC HALL
    choice=1
    while choice==1:
        try:
            print("***********************DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the hall number: "))
            q=("select * from event where hallno= %s")
            v=(n,)
            cur.execute(q,v)
            for (a,b,c,d,e,f,g) in cur:
                print()
                print("\tHall number: ",a)
                print("\tEvent type : ",b)
                print("\tCustomer's Adhaar no. : ",c)
                print("\tEmployee's code: ",d)
                print("\tHall rent: ",e)
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
    # FUNCTION TO DELETE A HALL
    choice=1
    while choice==1:
        try:
            print("***********************REMOVE EVENT DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the hall number: "))
            q=("delete from event where hallno=%s")
            v=(n,)
            cur.execute(q,v)
            db.commit()
            print("         HALL REMOVED!!!!")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue removing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("ROOMS DELETED!")



