import sys
import deposits_inrt
import deposits_select
import del_updt
import deposit_values
from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)


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
#        period= input("Enter the total number of duration for this FD : ")
        Principal_Amount= int(input("Enter the amount deposited for this FD : "))
        effect_from_date = input("Enter the date from when it gets effected in this format yy-m-d : ")
        maturity_date = input("Enter the date when the amount gets matured in this format yy-m-d : ")
        Maturity_Amount= int(input("Enter the total amount matured for this FD : "))
        Interest= float(input("Enter the interest rate for this FD : "))
        deposits_inrt.insert(Name,Account_No,Principal_Amount,effect_from_date,maturity_date,Maturity_Amount,Interest)
        break

    elif option == 2:
        data = deposits_select.select()
        deposits_select.show_table(data)
        sys.exit()

    elif option == 3:
        del_updt.update()
        sys.exit

    elif option == 4:
        id = int(input("Enter the id to delete : "))
        del_updt.delete(id)
        sys.exit

    elif option == 7:
        break

    elif option == 5:
        deposit_values.select1()
        sys.exit()

    elif option == 6:
        deposits_select.process_results()
        sys.exit

    else:
        print("Invalid option \n")
