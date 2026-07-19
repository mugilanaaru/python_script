from flask import Flask,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="home"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="select * from Tenants"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)

if (__name__ == '__main__'):
    app.run()