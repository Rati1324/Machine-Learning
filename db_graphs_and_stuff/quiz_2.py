import random as rn
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rati",
    password="123456",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO student (personal_id, sun, mon, tue, thu, wed, fri, sat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = []
for i in range(0, 10):
    days = []
    for j in range(7):
        days.append(round(rn.random() * 5, 2))
    values.append((rn.choice(range(100, 999)), *days))
print(values)
mycursor.executemany(sql, values)
mydb.commit()