from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)


def select1():
    print("To print the details of all accounts owned by a person - enter 'Name' : ")
    print("To print the details of a account - enter 'AC_No :  ")
    print("To print the details a account by paticular period - Enter 'period' : ")
    print("To print the details a account by paticular amount - Enter 'Principal_Amount' ")
    print("To print the details of a account by date - Enter 'effect_from_date'")
    print("To filter a account by its maturiy date - Enter 'maturity_date'")
    print("To filter a account by its maturiy account - Enter 'Maturity_Amount'")
    print("To filter a account by its Interest rate - Enter 'Interest'")
    option = input("\nwhich one you want to view : ")
    if option == 'Name':
       Name= input("Enter the Name: ")
    elif option == 'AC_No':
       Name = input("Enter the account number: ")
    elif option == "period":
       Name = input("Enter the period duration")
    elif option == "Principal_Amount":
       Name = input("Enter the amount to check")
    elif option == "effect_from_date":
       Name = input("Enter the date to check format should be 2025-11-10: ")
    elif option == "maturity_date":
       Name = input("Enter the maturity date to check format should be 2025-11-10: ")
    elif option == "Maturity_Amount":
       Name = input("Enter the amount to show : ")
    elif option == "Interest":
       Name = input("Enter the number to check : ")
    res=con.cursor()
    sql = f"select * from deposits where {option} like %s;"
    user=(Name)
    res.execute(sql,("%" + user + "%",))
    result=res.fetchall()
    print(tabulate(result,headers=["ID","Name","Account Number","period","Principal_Amount","effect_from_date","maturity_date","Maturity_Amount","Interest %"]))
    print("\n\n")