#PYTHON MODULE - CLIENT
import mysql.connector
def Showall():
#FUNCTION TO SHOW DETAILS OF ALL CLIENTS
    try:
        print("******************* DETAILS OF ALL CLIENTS *******************")
        db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
        cur=db.cursor()
        q=("Select * from custom")
        cur.execute(q)
        for (a,b,c,d,e,f,g,h,i) in cur:
            print()
            print("\tName: ",a)
            print("\tMobile no. : ",b)
            print("\tAdhaar no. : ",c)
            print("\tEmail : ",d)
            print("\tAddress : ",e)
            print("\tNo. of adults: ",f)
            print("\tNo. of children : ",g)
            if h==0:
                print("\tHall no : ",i)
            elif i==0:
                print("\tRoom no. : ",h)
            print()
    except:
        print("ERROR!!!!! PLEASE TRY AGAIN....")
        

def Show():
    #FUNCTION TO SHOW DETAILS OF A SPECIFIC CLIENT
    choice=1
    while choice==1:
        try:
            print("******************* DETAILS OF A CLIENT *******************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            v=input("Enter client's name : ")
            q=("Select * from custom where clname=%s")
            m=(v,)
            cur.execute(q,m)
            for (a,b,c,d,e,f,g,h,i) in cur:
                print()
                print("\tName: ",a)
                print("\tMobile no. : ",b)
                print("\tAdhaar no. : ",c)
                print("\tEmail : ",d)
                print("\tAddress : ",e)
                print("\tNo. of adults: ",f)
                print("\tNo. of children : ",g)
                if h==0:
                    print("\tHall no : ",i)
                elif i==0:
                    print("\tRoom no. : ",h)
                print()
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue viewing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print()

        
def Change():
    #FUNCTION TO CHANGE THE DETAILS OF A CLIENT
    choice=1
    while choice==1:
        try:
            print("******************* DETAILS OF A CLIENT *******************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            x=int(input("Enter the client adhaar no. whose details are to be changed: "))
            b=(x,)    
            print('''Select from the following (where the change has to be done)
    1.Name
    2.Phone number
    3.Email-ID
    4.Address
    5.No. of adults
    6.No. of children''')
           
            y=int(input("Enter your choice: "))
            if y==1:
                l=("select clname from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original name= ",d)
                p=input("Enter new name: ")
                q=("update custom set clname=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==2:
                l=("select clno from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original number= ",d)
                p=int(input("Enter new number: "))
                q=("update custom set clno=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==3:
                l=("select clemail from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original email= ",d)
                p=input("Enter new Email-ID: ")
                q=("update custom set clemail=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==4:
                l=("select address from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original address= ",d)
                p=input("Enter new Address: ")
                q=("update custom set address=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==5:
                l=("select noofadul from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of adults= ",d)
                p=int(input("Enter new No. of Adults : "))
                q=("update custom set noofadul=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
            elif y==6:
                l=("select noofchildren from custom where claadhar=%s")
                cur.execute(l,b)
                c=cur.fetchone()
                for d in c:
                    print("Original no. of children= ",d)
                p=int(input("Enter new No. of Children : "))
                q=("update custom set noofchildren=%s where claadhar=%s")
                t=(p,x)
                cur.execute(q,t)
                db.commit()
                print("Changes are done")
        
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue changing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("DETAILS CHANGED!")


def Remove():
    # FUNCTION TO DELETE A CLIENT'S DETAILS
    choice=1
    while choice==1:
        try:
            print("***********************REMOVE CLIENT DETAILS***********************")
            db=mysql.connector.connect(host="localhost",user="root",passwd="ayushmakhloga",database="hotelm")
            cur=db.cursor()
            n=int(input("Enter the adhaar number: "))
            q=("delete from custom where claadhar=%s")
            v=(n,)
            cur.execute(q,v)
            db.commit()
            print("           DETAILS REMOVED!!!!")
        except:
            print("ERROR!!!!! PLEASE TRY AGAIN....")
        print()
        print("Do you want to continue removing?")
        choice=int(input("Enter 1 for yes or 0 for no: "))
    else:
        print("DETAILS DELETED!")





