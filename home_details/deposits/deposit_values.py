from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)


def select1():
    print("\n To view a particular person's deposits - press '1' : \n")
    print("To view or filter a particular Account number - press '2'  :  \n")
    print("To view deposits by a particular period - press '3' : \n")
    print("To filter the details by paticular amount - press '4'  \n")
    print("To filter the details by a particular initial date - press '5' \n")
    print("To filter the details by a particular maturity date - press '6' \n")
    print("To filter the details by paticular maturity amount - press '7' \n")
    print("To filter the details by particular rate of interest - press '8' \n")
    print("To filter the details by a particular bank - press '9' \n")
    option = input("\nwhich one you want to view : ")
    if option == '1':
       options = "Name"
       Name= input("Enter the Name: ")
    elif option == '2':
       options = "AC_No"
       Name = input("Enter the account number: ")
    elif option == "3":
       options = "period"
       Name = input("Enter the period duration")
    elif option == "4":
       options = "Principal_Amount"
       Name = input("Enter the amount to check")
    elif option == "5":
       options = "effect_from_date"
       Name = input("Enter the date to check format should be 2025-11-10: ")
    elif option == "6":
       options = "maturity_date"
       Name = input("Enter the maturity date to check format should be 2025-11-10: ")
    elif option == "7":
       options = "Maturity_Amount"
       Name = input("Enter the amount to show : ")
    elif option == "8":
       options = "Interest"
       Name = input("Enter the interest to check : ")
    elif option == "9":
       options = "Bank_Name"
       Name = input("Enter the bank name to check : ")
    res=con.cursor()
    sql = f"select * from deposits where {options} like %s;"
    user=(Name)
    res.execute(sql,("%" + user + "%",))
    result=res.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","Name","Ac No","period","Amount","Start Date","Maturity Date","Maturity Amount","Interest","Bank"]))
    print("\n\n")