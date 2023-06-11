#PYTHON MODULE : EMPLOYEE
import mysql.connector
def Show():
    # FUNCTION TO SHOW DETAILS OF A CLIENT
    choice=1
    while choice==1:
        try:
            print("***********************DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the ECODE: "))
            q=("select * from employee where ecode= %s")
            v=(n,)
            cur.execute(q,v)
            for (a,b,c,d,e,f) in cur:
                print()
                print("Ecode: ",a)
                print("Name : ",b)
                print("Department: ",c)
                print("Mobile no.: ",d)
                print("Adhaar no.: ",e)
                print("E-mail: ",f)
                print()
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue viewing details?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print()

def Showall():
    # FUNCTION TO SHOW DETAILS OF ALL CLIENTS
    try:
        print("***********************DETAILS OF ALL EMPLOYEES***********************")
        db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
        cur=db.cursor()
        cur.execute("select * from employee")
        for (a,b,c,d,e,f) in cur:
            print()
            print("\tEcode: ",a)
            print("\tName : ",b)
            print("\tDepartment: ",c)
            print("\tMobile no.: ",d)
            print("\tAdhaar no.: ",e)
            print("\tE-mail: ",f)
            
    except:
        print("ERROR!!!!! PLEASE TRY AGAIN....")

def Add():
    # FUNCTION TO ADD AN EMPLOYEE
    choice=1
    while choice==1:
        try:
            print("***********************ADD AN EMPLOYEE'S DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            e=int(input("\tEnter the ecode: "))
            g=input("\tEnter employee's name: ")
            f=input("\tEnter department: ")
            h=int(input("\tEnter mobile no. : "))
            i=int(input("\tEnter adhaar no. : "))
            j=input("\tEnter e mail : ")
            v=(e,g,f,h,i,j)
            q=("insert into employee values(%s,%s,%s,%s,%s,%s)")
            cur.execute(q,v)
            db.commit()
            print()
            print("\tDetails added")
            print()
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue adding?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("DETAILS ADDED")

def Change():
    # FUNCTION TO CHANGE THE DETAILS OF AN EMPLOYEE
    choice=1
    while choice==1:
        try:
            print("***********************CHANGE AN EMPLOYEE'S DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("\tEnter the ecode: "))
            i=(n,)
            print()
            print("\tSelect from the following (where the change has to be done)")
            print("\t1.Name")
            print("\t2.Department")
            print("\t3.Mobile no.")
            print("\t4.Adhaar no.")
            print("\t5.E-mail")
            print()
            v=int(input("Enter your choice : "))
            if v==1:
                q=("select ename from employee where ecode=%s")
                cur.execute(q,i)
                c=cur.fetchone()
                for a in c:
                    print("Original name :",a)
                p=input("Enter new name : ")
                r=("update employee set ename=%s where ecode=%s")
                t=(p,n)
                cur.execute(r,t)
                db.commit()
                print("Changes are done")
            if v==2:
                q=("select dept from employee where ecode=%s")
                cur.execute(q,i)
                c=cur.fetchone()
                for a in c:
                    print("Original department :",a)
                p=input("Enter new department : ")
                r=("update employee set dept=%s where ecode=%s")
                t=(p,n)
                cur.execute(r,t)
                db.commit()
                print("Changes are done")
            if v==3:
                q=("select eno from employee where ecode=%s")
                cur.execute(q,i)
                c=cur.fetchone()
                for a in c:
                    print("Original number :",a)
                p=int(input("Enter new number : "))
                r=("update employee set eno=%s where ecode=%s")
                t=(p,n)
                cur.execute(r,t)
                db.commit()
                print("Changes are done")
            if v==4:
                q=("select eaadhar from employee where ecode=%s")
                cur.execute(q,i)
                c=cur.fetchone()
                for a in c:
                    print("Original adhaar no. :",a)
                p=int(input("Enter new adhaar no. : "))
                r=("update employee set eaadhar=%s where ecode=%s")
                t=(p,n)
                cur.execute(r,t)
                db.commit()
                print("Changes are done")
            if v==5:
                q=("select eemail from employee where ecode=%s")
                cur.execute(q,i)
                c=cur.fetchone()
                for a in c:
                    print("Original email :",a)
                p=input("Enter new email : ")
                r=("update employee set eemail=%s where ecode=%s")
                t=(p,n)
                cur.execute(r,t)
                db.commit()
                print("Changes are done")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue changing details?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("CHANGES DONE!")

def Remove():
    #FUNCTION TO DELETE AN EMPLOYEE'S DETAILS
    choice=1
    while choice==1:
        try:
            print("***********************DELETE AN EMPLOYEE'S DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the ecode : "))
            v=(n,)
            q=("delete from employee where ecode=%s")
            cur.execute(q,v)
            db.commit()
            print("     DETAILS DELETED")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue removing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("DETAILS DELETED!")
    

                

                


                

