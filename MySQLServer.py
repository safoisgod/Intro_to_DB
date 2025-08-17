import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your MySQL username
        password="your_password"  # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        cursor.close()

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close connection if it was opened
    if 'connection' in locals() and connection.is_connected():
        connection.close()