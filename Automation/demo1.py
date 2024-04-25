import mysql.connector

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='employees'
    )

    if connection.is_connected():
        print('Connected to MySQL database')

    # Perform database operations here

    cursor = connection.cursor()

    

    
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

