import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Pandalogo@789a",
        database="bank_system"
    )