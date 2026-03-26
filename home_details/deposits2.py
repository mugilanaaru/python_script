from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)


def select1():
    print("1.Name")
    print("8.Account_Number")
    print("2.period")
    print("3.Principal_Amount")
    print("4.effect_from_date")
    print("5.maturity_date")
    print("6.Maturity_Amount")
    print("7.Interest")
    option = int(input("\nwhich one you want to view : "))
    if option == 1:
        Name= input("Enter the Name: ")
        res=con.cursor()
        sql = "select * from deposits where Name=%s;"
        user=(Name)
        res.execute(sql,(user,))
        result=res.fetchall()
        print(tabulate(result,headers=["ID","Name","Account Number","period","Principal_Amount","effect_from_date","maturity_date","Maturity_Amount","Interest %"]))
        print("\n\n")

