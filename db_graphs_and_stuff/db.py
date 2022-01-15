import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="rati",
  password="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (f_name, l_name) VALUES (%s, %s)"
val = ("John", "Johnson")
mycursor.execute(sql, val)
mydb.commit()
