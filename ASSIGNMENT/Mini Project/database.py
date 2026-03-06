import mysql.connector

def save_mysql(data):

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )

    cursor=conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
    cursor.execute("USE studentdb")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks(
    roll INT,
    name VARCHAR(50),
    sub1 INT,
    sub2 INT,
    sub3 INT,
    total INT,
    avg FLOAT)
    """)

    sql="INSERT INTO marks VALUES(%s,%s,%s,%s,%s,%s,%s)"

    cursor.execute(sql,(
        data["Roll"],
        data["Name"],
        data["Subject1"],
        data["Subject2"],
        data["Subject3"],
        data["Total"],
        data["Average"]
    ))

    conn.commit()

    cursor.execute("SELECT * FROM marks")

    for row in cursor:
        print(row)

    conn.close()