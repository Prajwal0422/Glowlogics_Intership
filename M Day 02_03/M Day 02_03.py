import mysql.connector

database = mysql.connector.connect(host="localhost", user='root', passwd="122334")

cursorObject = database.cursor()

cursorObject.execute("Create databse Prajwal")

print("Databse created")