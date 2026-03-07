import mysql.connector

database = mysql.connector.connect(host="localhost", user='root', passwd="122334")

cursorObject = database.cursor()

s1="CREATE TABLE STUDENT (ROLL NO INT, NAME VARCHAR)"

cursorObject.execute("Create databse Prajwal")

database.close()

print("table created")