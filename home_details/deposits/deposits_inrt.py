import sys
import period_cal
from tabulate import tabulate
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)

def insert(Name, Account_no, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest, Bank_Name):
    res=con.cursor()
    period_days = period_cal.period(effect_from_date, maturity_date)
    sql="insert into deposits(Name, AC_No, period, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest, Bank_Name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    user=(Name, Account_no, period_days, Principal_Amount, effect_from_date, maturity_date, Maturity_Amount, Interest, Bank_Name)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfuly")
    print("\n\n\n")