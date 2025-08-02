from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="home")



def insert(date, Name, metre_number, current_reading, last_reading, total_reading, eb_amount, maintanence, total_amount):
    res=con.cursor()
    sql="insert into readings(date,Name,Meter_NO,Current_reading,Last_reading,Total_reading,EB_amount,maintanence,Total_amount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    user=(date,Name,metre_number,current_reading,last_reading,total_reading,eb_amount,maintanence,total_amount)
    try:
        res.execute(sql,user)
    except mysql.connector.Error as err:
        # handle date format error
        if err.errno == 1292:
            print("Date format error. Please use 'YYYY-MM-DD'.")
        else:
            print(f"Error: {err}")
        exit(1)
    con.commit()
    print("Data inserted successfuly")
    print("\n\n\n")

def select():
    res=con.cursor()
    sql="select * from  readings"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["date","Name","metre_number","current_reading","last_reading","total_reading","eb_amount","maintanence","total_amount"]))
    print("\n\n")

def update():
    print("1.date")
    print("2.metre_number")
    print("3.current_reading")
    print("4.last_reading")
    print("5.total_reading")
    print("6.eb_amount")
    print("7.maintanence")
    print("8.total_amount")
    option = int(input("\nwhich one you want to update : "))
    if option == 1:
        pid = input("Enter your id: ")
        date= input("Enter the date: ")
        cur = con.cursor()
        sql = "update readings set date=%s where ID=%s"
        cur.execute(sql,(date, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 2:
        pid = input("Enter your id: ")
        metre_number= input("Enter the meter_no: ")
        cur = con.cursor()
        sql = "update readings set Meter_NO=%s where ID=%s"
        cur.execute(sql,(metre_number, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 3:
        pid = input("Enter your id: ")
        current_reading = input("Enter the current reading to update : ")
        cur = con.cursor()
        sql = "update readings set Current_reading=%s where ID=%s"
        cur.execute(sql,(current_reading, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
    
    elif option == 5:
        pid = input("Enter your id: ")
        total_reading = input("Enter the total reading to update : ")
        cur = con.cursor()
        sql = "update readings set Total_reading=%s where ID=%s"
        cur.execute(sql,(total_reading, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 4:
        pid = input("Enter your id: ")
        last_reading = input("Enter the last reading to update : ")
        cur = con.cursor()
        sql = "update readings set Last_reading=%s where ID=%s"
        cur.execute(sql,(last_reading, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 6:
        pid = input("Enter your id: ")
        eb_amount = input("Enter the eb amount to update : ")
        cur = con.cursor()
        sql = "update readings set EB_Amount=%s where ID=%s"
        cur.execute(sql,(eb_amount, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
       
    elif option == 7:
        pid = input("Enter your id: ")
        maintanence = input("Enter the maintanance amount to update : ")
        cur = con.cursor()
        sql = "update readings set maintanence=%s where ID=%s"
        cur.execute(sql,(maintanence, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")   

    elif option == 8:
        pid = input("Enter your id: ")
        total_amount = input("Enter the total amount to update : ")
        cur = con.cursor()
        sql = "update readings set Total_Amount=%s where ID=%s"
        cur.execute(sql,(total_amount, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    else:
        print("Invalid Option")

def delete(id):
    res=con.cursor()
    sql="delete from readings where id=%s"
    user = (id,)   ### this is primary key so we are giving ,
    res.execute(sql, user)
    con.commit()
    print("Data deleted successfully")
    print("\n\n")

while True:
    print("1.Enter the values : \n")
    
    print("2.Show the EB data's : \n")

    print("3.Enter the values to update : \n")

    print("4:Enter the values to delete : \n")

    print("5.Exit \n")

    option = int(input("Enter the choice accordingly : "))
    if option == 1:
        date = input("Enter the date in this format yy-m-d : ")
        metre_number= int(input("Enter the meter number : "))
        current_reading=int(input("Enter the current month reading : "))
        last_reading=int(input("Enter the last month reading : "))
        total_reading= current_reading - last_reading
        eb_amount= total_reading * 6
        maintanence = int(input("Enter the maintanence amount : "))
        total_amount = eb_amount + maintanence
        if metre_number == 109:
            Name="Gunasekar"
        elif metre_number == 189:
            Name="Velu"
        elif metre_number == 191:
            Name="Thamizharasan"
        insert(date,Name,metre_number,current_reading,last_reading,total_reading,eb_amount,maintanence,total_amount)
        break

    elif option == 2:
        select()
        break
    
    elif option == 3:
        update()
        break

    elif option == 4:
        id = int(input("Enter the id to delete : "))
        delete(id)

    elif option == 5:
        break

    else:
        print("Invalid option \n")