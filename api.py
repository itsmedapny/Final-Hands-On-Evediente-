from flask import Flask, jsonify, make_response
from flask_mysqldb import MySQL

# access to database 
app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "genderanddevelopment"
app.config["MYSQL_DB"] = "classicmodels"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Select Statement 
@app.route("/customers", methods=["GET"])
def get_customers():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM customers"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return make_response(jsonify(data), 200)

# Flask Test
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)