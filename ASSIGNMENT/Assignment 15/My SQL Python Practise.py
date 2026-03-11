import mysql.connector

# Create Database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS apponix")
con.close()


# Create Table
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="apponix"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
NAME VARCHAR(20) NOT NULL,
BRANCH VARCHAR(50),
ROLL INT NOT NULL,
SECTION VARCHAR(5),
AGE INT
)
""")

# Insert Multiple Records
sql = """INSERT INTO STUDENT
(NAME,BRANCH,ROLL,SECTION,AGE)
VALUES (%s,%s,%s,%s,%s)"""

val = [
("Nikhil","CSE",98,"A",18),
("Nisha","CSE",99,"A",18),
("Rohan","MAE",43,"B",20),
("Amit","ECE",24,"A",21),
("Anil","MAE",45,"B",20),
("Megha","ECE",55,"A",22),
("Sita","CSE",95,"A",19)
]

cur.executemany(sql,val)
con.commit()

# Select Records
cur.execute("SELECT NAME,ROLL FROM STUDENT")

result = cur.fetchall()

for row in result:
    print(row)

con.close()