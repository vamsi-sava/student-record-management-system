import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "vamsi@1431",
        database = "student_db"
    )

    return connection