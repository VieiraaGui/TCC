import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='34.95.209.0',
                                         database='dados',
                                         user='root',
                                         password='')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectou foda no google ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")