
import numpy as np
import pandas as pd
from sklearn import tree
import graphviz
import mysql.connector
from sqlalchemy import create_engine
mydb = mysql.connector.connect(
    user="root",
    password = "",
    host = "34.95.209.0",
    database = 'dados'
)

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
data = pd.read_sql('select * from CPU', mydb)
print(data)

print("////////////////////////////////////////////n")
teste2 = pd.read_sql('select * from GPU', mydb)

teste22 = pd.read_sql('select * from MOBO', mydb)
teste = pd.read_sql('select * from RAM', mydb)
dataRam = pd.read_sql('select ramName, ramPrice, ramSize, ramAvailability, store from RAM where ramAvailability = '
                      '"DISPONIVEl"', mydb)
dataCpu = pd.read_sql('select cpuName, cpuPrice, cpuSocket, store, from CPU where cpuAvailability  = '
                      '"DISPONIVEl"', mydb)
print(dataCpu)


