from flask import Flask, render_template,url_for,redirect,request,flash
from datetime import date, datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

from utils.period_cal import calculate_period   #### module for date difference calculate
#from deposits import deposits_bp
import pymysql          #####  module for mysql connect
import configparser     ##### module for config.ini file
from werkzeug.utils import secure_filename
from db import get_connection


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))

#def get_connection():
#    parser = configparser.ConfigParser()
#    parser.read("db_config.ini")
#
#    return pymysql.connect(
#        host=parser["mysql"]["host"],
#        user=parser["mysql"]["user"],
#        password=parser["mysql"]["password"],
#        database=parser["mysql"]["database"],
#        cursorclass=pymysql.cursors.DictCursor
#    )

##def get_connection():
##    return pymysql.connect(
##        host=os.getenv("DB_HOST", "db"),        # default to "db"
##        user=os.getenv("DB_USER", "root"),
##        password=os.getenv("DB_PASSWORD", "root"),
##        database=os.getenv("DB_NAME", "home"),
##        port=int(os.getenv("DB_PORT", 3306)),
##        cursorclass=pymysql.cursors.DictCursor
##    )

##########################################

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            # normalize filename
            filename = secure_filename(file.filename)
            filename = filename.lower()   # force lowercase filename

            # extract extension safely
            ext = filename.rsplit('.', 1)[1] if '.' in filename else ''

            if ext in ALLOWED_EXTENSIONS:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash(f"File {filename} uploaded successfully!")
                return redirect(url_for('home'))
            else:
                flash("Invalid file type")
                return redirect(url_for('upload'))
    return render_template("upload.html")

############################################

@app.route("/")
def home():
    # list all files in static/uploads
    files = os.listdir("static/uploads")
    return render_template("home.html", files=files)


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

#################  Tenants toggle button for active in active ###########
@app.route("/toggle/<int:id>")
def toggle_status(id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT is_active FROM Tenants WHERE ID=%s", (id,))
            current = cursor.fetchone()["is_active"]

            new_status = 0 if current == 1 else 1
            cursor.execute("UPDATE Tenants SET is_active=%s WHERE ID=%s", (new_status, id))
            conn.commit()
    finally:
        conn.close()
    return redirect(url_for("list_tenents"))


###########
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

    # Convert maturity_date to a proper date object if it’s a string        #### newly added for maturity date to show warning
    for row in res:
        if isinstance(row['maturity_date'], str):
            row['maturity_date'] = datetime.strptime(row['maturity_date'], "%Y-%m-%d").date()

    # Pass both today and threshold date (today + 30 days)
    return render_template(
        "deposits.html",
        datas=res,
        current_date=date.today(),
        threshold_date=date.today() + timedelta(days=30))
    #return render_template("deposits.html", datas=res)     #### normal on commented out

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
        return redirect(url_for("home_deposits"))
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
@app.route("/edit/<string:table>/<string:id>", methods=['GET','POST'])
def edituser(table, id):
    conn = get_connection()
    if request.method == 'POST':
        with conn.cursor() as cursor:
            if table == "Tenants":
                NAME = request.form['NAME']
                Advance = request.form['Advance']
                EB_Number = request.form['EB_Number']
                sql = "UPDATE Tenants SET NAME=%s, Advance=%s, EB_Number=%s WHERE ID=%s"
                cursor.execute(sql, [NAME, Advance, EB_Number, id])

            elif table == "deposits":
                Name = request.form['Name']
                Account_Number = request.form['Account_Number']
                Principal_Amount = request.form['Principal_Amount']
                Date = request.form['Date']
                Maturity_Date = request.form['Maturity_Date']
                Maturity_Amount = request.form['Maturity_Amount']
                Interest_Rate=request.form['Interest_Rate']
                Bank_Details = request.form['Bank_Details']

                # Call helper function to calculate period
                period_days, period_readable = calculate_period(Date, Maturity_Date)

                # Decide what to store (days or readable string)
                period = period_readable   # or use period_readable

                sql = "UPDATE deposits SET Name=%s, AC_No=%s, period=%s, Principal_Amount=%s, effect_from_date=%s, Maturity_Date=%s, Maturity_Amount=%s, Interest=%s, Bank_Name=%s  WHERE ID=%s"
                cursor.execute(sql, [Name, Account_Number, period, Principal_Amount, Date, Maturity_Date, Maturity_Amount, Interest_Rate, Bank_Details, id])

            elif table == "readings":
                Date = request.form['Date']
                Current_reading = request.form['Current_reading']
                Last_reading = request.form['Last_reading']
                total_reading= int(Current_reading) - int(Last_reading)
                eb_amount= total_reading * 6
                #    maintanence = int(input("Enter the maintanence amount : "))
                maintanence = 350
                total_amount = int(eb_amount) + int(maintanence)
                sql = "UPDATE readings SET Date=%s, Current_reading=%s, Last_reading=%s, total_reading=%s, eb_amount=%s, total_amount=%s  WHERE ID=%s"
                cursor.execute(sql, [Date, Current_reading, Last_reading, total_reading, eb_amount, total_amount, id])

            else:
                flash("Invalid table specified")
                return redirect(url_for("home"))

        conn.commit()
        conn.close()
        flash(f"{table} record updated")
        return redirect(url_for("home"))

    # GET request: fetch record for pre-filling form
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM {table} WHERE ID=%s"
        cursor.execute(sql, [id])
        res = cursor.fetchone()
    conn.close()

    return render_template("useredit.html", datas=res, table=table)


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


###################### Adding for filter ##############################
@app.route("/filter_deposits", methods=['GET', 'POST'])
def filter_deposits():
    if request.method == 'POST':
        option = request.form['option']
        value = request.form['value']
        return redirect(url_for('filter_results', option=option, value=value))
    return render_template("filter_deposits.html")

###################  Addng filter results ##############################
@app.route("/filter_results")
def filter_results():
    option = request.args.get('option')
    value = request.args.get('value')

    mapping = {
        '1': 'Name',
        '2': 'AC_No',
        '3': 'period',
        '4': 'Principal_Amount',
        '5': 'effect_from_date',
        '6': 'maturity_date',
        '7': 'Maturity_Amount',
        '8': 'Interest',
        '9': 'Bank_Name'
    }
    column = mapping.get(option)

    results = []
    if column:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM deposits WHERE {column} LIKE %s"
                cursor.execute(sql, ("%" + value + "%",))
                results = cursor.fetchall()
        finally:
            conn.close()

    return render_template("filter_results.html", datas=results)

######################### deposits summary ###############################
@app.route("/deposits_summary")
def deposits_summary():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Group deposits by Name and sum the Principal_Amount
            sql = """
                SELECT Name, SUM(Principal_Amount) AS total_amount
                FROM deposits
                GROUP BY Name
            """
            cursor.execute(sql)
            res = cursor.fetchall()
    finally:
        conn.close()

    return render_template("deposits_summary.html", datas=res)


## Register blueprints
#app.register_blueprint(deposits_bp)

if __name__ == "__main__":
#    app.secret_key="abc123"
    app.run(debug=True)