import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Tcc',
                                         user='root',
                                         password='')
    if connection.is_connected():
        print("Sucesso !")
except Error as e:
    print("Error while connecting to MySQL", e)



