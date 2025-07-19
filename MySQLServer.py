import mysql.connector
from mysql.connector import Error
import getpass

try:
    db_password = getpass.getpass("Enter MySQL password: ")
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        port= 3307,
        password=db_password
    )
    
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        

except Error as err:
    # If any error happens (wrong password, MySQL not running, etc.)
    print(f"Error: {err}")
    
finally:
    # Clean up: close the cursor if it was created
    if 'cursor' in locals():
        cursor.close()

    # Close the mydb if it was created and is still open
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()