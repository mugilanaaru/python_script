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
def addusers():
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

            else:
                flash('Invalid table specified')

        conn.commit()
    finally:
        conn.close()
    return redirect(url_for("home"))

## Register blueprints
#app.register_blueprint(deposits_bp)

if __name__ == "__main__":
    app.secret_key="abc123"
    app.run(debug=True)
