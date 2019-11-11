import os

import numpy as np
import pandas as pd
from sklearn import tree
import graphviz
import mysql.connector
from sqlalchemy import create_engine

mydb = mysql.connector.connect(
    user="root",
    password="",
    host="34.95.209.0",
    database='dados'
)

dataCpu = pd.read_sql('select cpuName, cpuPrice, cpuSocket, store, cpuAvailability from CPU', mydb)
dataGpu = pd.read_sql('select * from GPU', mydb)
dataMobo = pd.read_sql('select * from MOBO', mydb)
dataRam = pd.read_sql('select * from RAM', mydb)

socket = []
for dado in dataCpu['cpuSocket'].dropna():
    socket.append(dado)

nameP = []
for dado in dataCpu['cpuName'].dropna():
    nameP.append(dado)

precoP = []
for dado in dataCpu['cpuPrice'].dropna():
    precoP.append(dado)

lojaP = []
for dado in dataCpu['store'].dropna():
    lojaP.append(dado)

disp = []
for dado in dataCpu['cpuAvailability'].dropna():
    disp.append(dado)


cpu = {'Nome Produto': nameP, 'Preço ': precoP, 'Socket: ': socket, 'Loja ': lojaP, 'Situação': disp}
comp = pd.DataFrame(data=cpu)


##################################

socket = []
for dado in dataGpu['cpuSocket'].dropna():
    socket.append(dado)

nameP = []
for dado in dataGpu['cpuName'].dropna():
    nameP.append(dado)

precoP = []
for dado in dataGpu['cpuPrice'].dropna():
    precoP.append(dado)

lojaP = []
for dado in dataGpu['store'].dropna():
    lojaP.append(dado)

disp = []
for dado in dataGpu['cpuAvailability'].dropna():
    disp.append(dado)


gpu = {'Nome Produto': nameP, 'Preço ': precoP, 'Socket: ': socket, 'Loja ': lojaP, 'Situação': disp}
comp = pd.DataFrame(data=cpu)



# # Testando a árvore
# features = list(comp.columns[1:2])
# testTree = comp[features]
#
# result = clf.predict(testTree)
#
# i = 0
#
#
# def verificaSocket(r):
#     if r[1] == 'AM4':
#         return "Socket AMD"
#     elif r[2] == '1151' or r[2] == '1151 v2':
#         return "Socket Intel"
#
#
# for resp in result:
#     print(str(product[i]) + '-' + verificaSocket(resp))
