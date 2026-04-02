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

def insert(Name, Account_no, period, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest):
    res=con.cursor()
    sql="insert into deposits(Name, AC_No, period, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    user=(Name, Account_no, period, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfuly")
    print("\n\n\n")

def select():
    res=con.cursor()
    sql="select * from deposits"
    res.execute(sql)
    result=res.fetchall()
#    print(tabulate(result,headers=["ID","Name","Account Number","period","Principal_Amount","effect_from_date","maturity_date","Maturity_Amount","Interest %"]))
    print("\n\n")
    return result

def show_table(data):
    print(tabulate(data, headers=[
        "ID","Name","Account Number","period",
        "Principal_Amount","effect_from_date",
        "maturity_date","Maturity_Amount","Interest %"
    ]))
    print("\n\n")

def process_results():
    data = select()   # call the first function
    total_amount = 0

    # Loop through the rows
    for row in data:
        total_amount += row[4]
    print(f"Total deposited amount : {total_amount}")

def update():
    print("1.Name")
    print("8.Account_Number")
    print("2.period")
    print("3.Principal_Amount")
    print("4.effect_from_date")
    print("5.maturity_date")
    print("6.Maturity_Amount")
    print("7.Interest")
    option = int(input("\nwhich one you want to update : "))
    if option == 1:
        pid = input("Enter your id: ")
        date= input("Enter the Name: ")
        cur = con.cursor()
        sql = "update deposits set Name=%s where ID=%s"
        cur.execute(sql,(date, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 2:
        pid = input("Enter your id: ")
        period_date= input("Enter the period: ")
        cur = con.cursor()
        sql = "update deposits set period=%s where ID=%s"
        cur.execute(sql,(period_date, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 3:
        pid = input("Enter your id: ")
        principal_amount = input("Enter the Principal Amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Principal_Amount=%s where ID=%s"
        cur.execute(sql,(principal_amount, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
    
    elif option == 4:
        pid = input("Enter your id: ")
        effect_date = input("Enter the date from when it effect from to update : ")
        cur = con.cursor()
        sql = "update deposits set effect_from_date=%s where ID=%s"
        cur.execute(sql,(effect_date, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 5:
        pid = input("Enter your id: ")
        mature_date = input("Enter the maturity date to update : ")
        cur = con.cursor()
        sql = "update deposits set maturity_date=%s where ID=%s"
        cur.execute(sql,(mature_date, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 6:
        pid = input("Enter your id: ")
        maturity_amount = input("Enter the eb Maturity Amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Maturity_Amount=%s where ID=%s"
        cur.execute(sql,(maturity_amount, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")
       
    elif option == 7:
        pid = input("Enter your id: ")
        interest = input("Enter the Interest amount to update : ")
        cur = con.cursor()
        sql = "update deposits set Interest=%s where ID=%s"
        cur.execute(sql,(interest, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    elif option == 8:
        pid = input("Enter your id: ")
        interest = input("Enter the Account Number to update : ")
        cur = con.cursor()
        sql = "update deposits set AC_No=%s where ID=%s"
        cur.execute(sql,(interest, pid))
        con.commit()
        select()
        print("\n")
        print("Updated successfully")

    else:
        print("Invalid Option")

def delete(id):
    res=con.cursor()
    sql="delete from deposit where id=%s"
    user = (id,)   ### this is primary key so we are giving ,
    res.execute(sql, user)
    con.commit()
    print("Data deleted successfully")
    print("\n\n")


while True:
    print("To insert the values - press 1 : \n")
    
    print("To print all the Deposits - press 2 : \n")

    print("To update deposit values - press 3 : \n")

    print("To delete the deposit values - press 4 : \n")

    print("To print the deposit values example:Name, AC_no - press 5 : \n")

    print("To print the total amount in deposit - press 6 : \n")

    print("7.Exit \n")

    option = int(input("Enter the choice accordingly : "))
    if option == 1:
        Name= input("Enter the AC holder name : ")
        Account_No= int(input("Enter the Account number for this FD : "))
        period= input("Enter the total number of duration for this FD : ")
        Principal_Amount= int(input("Enter the amount deposited for this FD : "))
        effect_from_date = input("Enter the date from when it gets effected in this format yy-m-d : ")
        maturity_date = input("Enter the date when the amount gets matured in this format yy-m-d : ")
        Maturity_Amount= int(input("Enter the total amount matured for this FD : "))
        Interest= float(input("Enter the interest rate for this FD : "))
        insert(Name,Account_No,period,Principal_Amount,effect_from_date,maturity_date,Maturity_Amount,Interest)
        break

    elif option == 2:
        data = select()
        show_table(data)
        sys.exit()

    elif option == 3:
        deposits_update.update()
        break

    elif option == 4:
        id = int(input("Enter the id to delete : "))
        delete(id)
        break

    elif option == 7:
        break

    elif option == 5:
        deposits_select.select1()
        sys.exit()

    elif option == 6:
        process_results()
        break

    else:
        print("Invalid option \n")
