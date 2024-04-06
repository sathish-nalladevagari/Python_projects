
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password123"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
print("All done") 