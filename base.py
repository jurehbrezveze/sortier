import mysql.connector

mydb = mysql.connector.connect(
  host="10.1.1.2",
  user="sorter",
  password="Mk0ck3l!",
  database = "sorter"
)

c = mydb.cursor()

def insert(id,path):
    q = f"INSERT INTO paths (brick_id,path) VALUES ({id},{path})"
    c.execute(q)
    mydb.commit()

def read():
    q = f"SELECT * FROM paths"
    c.execute(q)
    r = c.fetchall()
    for x in r:
        print(x)

def format():
    q = f"DELETE FROM paths"
    c.execute(q)
    mydb.commit()


read()