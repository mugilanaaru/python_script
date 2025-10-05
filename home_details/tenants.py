from tabulate import tabulate
#import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="home")

"""
if con:
    print("connected")
else:
    print("connection error")
"""
def insert(name, advance, eb_number):
    res=con.cursor()
    sql="insert into Tenants(NAME,Advance,EB_number) values (%s,%s,%s)"
    user=(name,advance,eb_number)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfuly")
    print("\n\n\n")
    
def update():
    print("1.Name")
    print("2.Advance")
    print("3.EB_number")
    print("4.date_araived")
    option = int(input("\nwhich one you want to update : "))
    if option == 1:
        pid = input("Enter your id: ")
        name= input("Enter youe name: ")
        cur = con.cursor()
        sql = "update Tenants set name=%s where ID=%s"
        cur.execute(sql,(name, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
    
    elif option == 2:
        pid = input("Enter your id: ")
        advance= input("Enter your advance amount to update:  ")
        cur = con.cursor()
        sql = "update Tenants set Advance=%s where ID=%s"
        cur.execute(sql,(advance, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
    
    elif option == 3:
        pid = input("Enter your id: ")
        eb_number= input("Enter your EB number to update:  ")
        cur = con.cursor()
        sql = "update Tenants set EB_Number=%s where ID=%s"
        cur.execute(sql,(eb_number, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 4:
        pid = input("Enter your id: ")
        date = input("Enter the date to update:  ")
        cur = con.cursor()
        sql = "update Tenants set date_araived=%s where ID=%s"
        cur.execute(sql,(date, pid))
        con.commit()
        select()
        print("\n") 
        print("Updated successfully")
    else:
        print("Invalid option")
    
def select():
    res=con.cursor()
    sql="SELECT * from Tenants"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","ADVANCE","EB Number","DATE"]))
    print("\n\n")

def delete(id):
    res=con.cursor()
    sql="delete from Tenants where id=%s"
    user = (id,)   ### this is primary key so we are giving ,
    res.execute(sql, user)
    con.commit()
    print("Data deleted successfully")
    print("\n\n")

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter the Name : ")
        advance = input("Enter the Advance amount: ")
        eb_number = input("Enter the EB number : ")
        insert(name,advance,eb_number)
    
    elif choice == 2:
        update()

    elif choice == 3:
        select()
        break

    elif choice == 4:
        id=input("Enter the id to delete : ")
        delete(id)
        break

    elif choice == 5:
        break
    else:
        print("invalid selection")