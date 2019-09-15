import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Tcc',
                                         user='root',
                                             password='')
    if connection.is_connected():
        connec = connection.get_server_info()
        print("Sucesso  e a versão do mysql é! ", connec)
except Error as e:
    print("Error while connecting to MySQL", e)

cursor = connection.cursor()
cursor.execute('select * from CPU')
print(cursor.fetchall())




