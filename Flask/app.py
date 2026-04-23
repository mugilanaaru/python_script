from flask import Flask, render_template,url_for,redirect,request
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
        return redirect(url_for("home"))
    return render_template("add_user.html")

#edit user
@app.route("/useredit/<string:id>",methods=['GET','POST'])

def edituser(id):
    conn = get_connection()
    with conn.cursor() as cursor:
            sql = "SELECT * FROM Tenants where ID=%s"
            cursor.execute(sql,[id])
            res = cursor.fetchone()
    return render_template("useredit.html",datas=res)

if __name__ == "__main__":
    app.run(debug=True)
