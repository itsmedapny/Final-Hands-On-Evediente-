from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL

# access to database 
app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "genderanddevelopment"
app.config["MYSQL_DB"] = "classicmodels"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Flask Test
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" 

# Select Statement 
@app.route("/customers", methods=["GET"])
def get_customers():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM customers"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return make_response(jsonify(data), 200)

# Update Statement
@app.route("/customers/update", methods=["GET"])
def update_customer():
    cur = mysql.connection.cursor()
    query = "UPDATE customers SET city='Philippines' WHERE customerNumber = 112"
    cur.execute(query)
    mysql.connection.commit()

    # Fetch the updated row 

    select_query = "SELECT * FROM customers WHERE customerNumber = 103"
    cur.execute(select_query)
    updated_data = cur.fetchone()

    cur.close()
    return make_response(jsonify(updated_data), 200)

# Join Statement 
@app.route("/customers/join", methods=["GET"])
def join_customer():
    cur = mysql.connection.cursor()
    query = """SELECT c.customerNumber, b.customerNumber, c.customerName, b.customerName, c.country, b.country
    FROM customers c, customers b WHERE c.country = b.country"""
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return make_response(jsonify(data), 200)

# Insert Into Statement using POST method
@app.route("/payments/amount", methods=["POST"])
def insert_payment():
    info = request.get_json()
    cur = mysql.connection.cursor()
    amount = info["amount"]
    cur.execute(
        """INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) 
        VALUES (112, "H556890", "2004-10-25", %s);""",
        (amount,)
    )
    mysql.connection.commit()
    cur.close()
    return make_response(
        jsonify({"message": "Payment added successfully"}), 201
    )

# Update statement using PUT method 
@app.route("/payments/<string:checkNumber>", methods=["PUT"])
def update_payment(checkNumber):
    cur = mysql.connection.cursor()
    info = request.get_json()
    amount = info["amount"]
    cur.execute(
        """UPDATE payments 
        SET amount = %s 
        WHERE checkNumber = %s;""", (amount, checkNumber)
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"Note": "The amount in payment updated successfully"}), 200
    )

# Delete Statement Using DELETE method
@app.route("/payments/<string:checkNumber>", methods=["DELETE"])
def delete_payment(checkNumber):
    cur = mysql.connection.cursor()
    cur.execute( """DELETE FROM payments
     where checkNumber = %s""", (checkNumber,)
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"Note": "The checkNumber in payment deleted successfully"}), 200
    )

if __name__ == "__main__":
    app.run(debug=True)