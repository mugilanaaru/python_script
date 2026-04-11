import sys
import deposits_select
import deposits_update
from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)

def update():
    print("1.Name")
    print("8.Account_Number")
    print("2.period")
    print("3.Principal_Amount")
    print("4.effect_from_date")
    print("5.maturity_date")
    print("6.Maturity_Amount")
    print("7.Interest")
    print("9.Bank Name")
    print("10.Exit")
    option = int(input("\nwhich one you want to update : "))
    if option == 1:
        pid = input("Enter your id: ")
        date= input("Enter the Name: ")
        cur = con.cursor()
        sql = "update deposits set Name=%s where ID=%s"
        cur.execute(sql,(date, pid))
        con.commit()
        data = deposits_select.select()
        deposits_select.show_table(data)
        print("\n")
        print("Updated successfully")
        update()

    elif option == 2:
        pid = input("Enter your id: ")
        period_date= input("Enter the period: ")
        cur = con.cursor()
        sql = "update deposits set period=%s where ID=%s"
        cur.execute(sql,(period_date, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 3:
        pid = input("Enter your id: ")
        principal_amount = input("Enter the Principal Amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Principal_Amount=%s where ID=%s"
        cur.execute(sql,(principal_amount, pid))
        con.commit()
        data = deposits_select.select()
        deposits_select.show_table(data)
        print("\n")
        print("Updated successfully")
        update()
    
    elif option == 4:
        pid = input("Enter your id: ")
        effect_date = input("Enter the date from when it effect from to update : ")
        cur = con.cursor()
        sql = "update deposits set effect_from_date=%s where ID=%s"
        cur.execute(sql,(effect_date, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 5:
        pid = input("Enter your id: ")
        mature_date = input("Enter the maturity date to update : ")
        cur = con.cursor()
        sql = "update deposits set maturity_date=%s where ID=%s"
        cur.execute(sql,(mature_date, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 6:
        pid = input("Enter your id: ")
        maturity_amount = input("Enter the eb Maturity Amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Maturity_Amount=%s where ID=%s"
        cur.execute(sql,(maturity_amount, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()
       
    elif option == 7:
        pid = input("Enter your id: ")
        interest = input("Enter the Interest amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Interest=%s where ID=%s"
        cur.execute(sql,(interest, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 8:
        pid = input("Enter your id: ")
        interest = input("Enter the Account Number to update : ")
        cur = con.cursor()
        sql = "update deposits set AC_No=%s where ID=%s"
        cur.execute(sql,(interest, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 9:
        pid = input("Enter your id: ")
        bank_name = input("Enter the Bank Name : ")
        cur = con.cursor()
        sql = "update deposits set Bank_Name=%s where ID=%s"
        cur.execute(sql,(bank_name, pid))
        con.commit()
        deposits_select.select()
        print("\n")
        print("Updated successfully")
        update()

    elif option == 10:
        sys.exit

    else:
        print("Invalid Option")

def delete(id):
    res=con.cursor()
    sql="delete from deposits where id=%s"
    user = (id,)   ### this is primary key so we are giving ,
    res.execute(sql, user)
    con.commit()
    print("Data deleted successfully")
    print("\n\n")
