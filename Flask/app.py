from flask import Flask, render_template,url_for,redirect,request,flash
from utils.period_cal import calculate_period
#from deposits import deposits_bp
import pymysql

app = Flask(__name__)

# Create a reusable connection function
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="home",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Tenants"
            cursor.execute(sql)
            res = cursor.fetchall()
    finally:
        conn.close()
    return render_template("home.html", datas=res)


#### List Tenents
@app.route("/list_tenents")
def list_tenents():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Tenants"
            cursor.execute(sql)
            res = cursor.fetchall()
    finally:
        conn.close()
    return render_template("list_tenents.html", datas=res)


#### for deposits
@app.route("/deposits")
def home_deposits():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM deposits"
            cursor.execute(sql)
            res = cursor.fetchall()
    finally:
        conn.close()
    return render_template("deposits.html", datas=res)

@app.route("/add_deposits",methods=['GET','POST'])
def adddeposits():
    if request.method=='POST':
        Name=request.form['Name']
        Account_Number=request.form['Account_Number']
#        period=request.form['period']
        Principal_Amount=request.form['Principal_Amount']
        Date=request.form['Date']
        Maturity_Date=request.form['Maturity_Date']
        Maturity_Amount=request.form['Maturity_Amount']
        Interest_Rate=f"{request.form['Interest_Rate']}%"
        Bank_Details=request.form['Bank_Details']

        # Call helper function to calculate period
        period_days, period_readable = calculate_period(Date, Maturity_Date)

        # Decide what to store (days or readable string)
        period = period_readable   # or use period_readable

        conn= get_connection()
        with conn.cursor() as cursor:
            sql="insert into deposits(Name,AC_NO,period,Principal_Amount, effect_from_date,maturity_date,Maturity_Amount,Interest,Bank_Name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,[Name,Account_Number,period,Principal_Amount,Date,Maturity_Date,Maturity_Amount,Interest_Rate,Bank_Details])
        conn.commit()
        conn.close()
        flash('User details added')
        return redirect(url_for("deposits"))
    return render_template("add_deposits.html")

#user insert
@app.route("/add_user",methods=['GET','POST'])
def add_tenents():
    if request.method=='POST':
        NAME=request.form['NAME']
        Advance=request.form['Advance']
        EB_Number=request.form['EB_Number']
        conn= get_connection()
        with conn.cursor() as cursor:
            sql="insert into Tenants(NAME,Advance,EB_number) values (%s,%s,%s)"
            cursor.execute(sql,[NAME,Advance,EB_Number])
        conn.commit()
        conn.close()
        flash('User details added')
        return redirect(url_for("home"))
    return render_template("add_user.html")

#edit user
@app.route("/useredit/<string:id>",methods=['GET','POST'])

def edituser(id):

    if request.method=='POST':
        NAME=request.form['NAME']
        Advance=request.form['Advance']
        EB_Number=request.form['EB_Number']
        conn= get_connection()
        with conn.cursor() as cursor:
            sql="update Tenants set NAME=%s,Advance=%s,EB_Number=%s where ID=%s"
            cursor.execute(sql,[NAME,Advance,EB_Number,id])
        conn.commit()
        conn.close()
        flash("user details updated")
        return redirect(url_for("home"))
    
    conn = get_connection()
    with conn.cursor() as cursor:
            sql = "SELECT * FROM Tenants where ID=%s"
            cursor.execute(sql,[id])
            res = cursor.fetchone()
    return render_template("useredit.html",datas=res)

# Delete User
#@app.route("/deleteuser/<string:id>",methods=['GET','POST'])
@app.route("/deleteuser/<string:id>/<string:table>", methods=['GET','POST'])
def deleteuser(id, table):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            if table == "Tenants":
                sql = "DELETE FROM Tenants WHERE ID=%s"
                cursor.execute(sql, (id,))
                flash('Tenant details deleted')

            elif table == "deposits":
                sql = "DELETE FROM deposits WHERE ID=%s"
                cursor.execute(sql, (id,))
                flash('Deposit record deleted')

            elif table == "readings":
                sql = "DELETE FROM readings WHERE ID=%s"
                cursor.execute(sql, (id,))
                flash('readings record deleted')

            else:
                flash('Invalid table specified')

        conn.commit()
    finally:
        conn.close()
    return redirect(url_for("home"))

###### EB Readings list #########
@app.route("/list_readings")
def list_readings():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM readings"
            cursor.execute(sql)
            res = cursor.fetchall()
    finally:
        conn.close()
    return render_template("list_readings.html", datas=res)


###### EB Readings ###########################

@app.route("/add_readings",methods=['GET','POST'])
def add_readings():
    if request.method=='POST':
        Date=request.form['Date']
        Meter_Number=request.form['Meter_Number']
        Current_reading=request.form['Current_reading']
        Last_reading=request.form['Last_reading']
        total_reading= int(Current_reading) - int(Last_reading)
        eb_amount= total_reading * 6
    #    maintanence = int(input("Enter the maintanence amount : "))
        maintanence = 350
        total_amount = int(eb_amount) + int(maintanence)
        names = {
            "109": "Gunasekar",
            "189": "Velu",
            "191": "Indumathi Tamizharasan",
            "190": "Sampath",
            "192": "Priya"
}
        Name = names.get(Meter_Number, "Unknown")

        conn= get_connection()
        with conn.cursor() as cursor:
            sql="insert into readings(Date,Name,Meter_NO,Current_reading,Last_reading,Total_reading,EB_Amount,maintanence,Total_Amount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,[Date,Name,Meter_Number,Current_reading,Last_reading,total_reading,eb_amount,maintanence,total_amount])
        conn.commit()
        conn.close()
        flash('EB details added')
        return redirect(url_for("list_readings"))
    return render_template("add_readings.html")

## Register blueprints
#app.register_blueprint(deposits_bp)

if __name__ == "__main__":
    app.secret_key="abc123"
    app.run(debug=True)
