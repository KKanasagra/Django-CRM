import mysql.connector

config = {
    'user': 'root',          # Replace with your MySQL username
    'password': 'root',  # Replace with your MySQL password
    'host': 'localhost',          # Replace with your MySQL host
    'auth_plugin': 'mysql_native_password'  # Explicitly specify the authentication method.
}

try:
    dataBase = mysql.connector.connect(**config)
    cursor = dataBase.cursor()

    # preparing a cursor object
    cursorObject = dataBase.cursor()
    
    # creating database
    cursorObject.execute("CREATE DATABASE project");

    dataBase.close()  # Close the database connection when done.

except mysql.connector.Error as err:
    print(f"Error: {err}")