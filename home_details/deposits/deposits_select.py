from tabulate import tabulate
from textwrap import shorten
import mysql.connector
import json
# Load config from file
with open("db_config.json") as f:
    config = json.load(f)
con = mysql.connector.connect(**config)

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
        "ID","Name","Ac No","period",
        "Amount","Start Date",
        "maturity_date","Maturity_Amount","Interest %","Bank"
    ], tablefmt="github"))
    print("\n\n")

def process_results():
    data = select()   # call the first function
    total_amount = 0

    # Loop through the rows
    for row in data:
        total_amount += row[4]
    print(f"Total deposited amount : {total_amount}")