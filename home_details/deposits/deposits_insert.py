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