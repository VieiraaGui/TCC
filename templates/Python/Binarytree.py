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

engine = create_engine('mysql+mysqlconnector://'+os.environ['root']+':'+os.environ['']+'@'+os.environ['34.95.209.0']+':'+os.environ['MYSQL_PORT']+'/sandbox', echo=False)

product = data = pd.read_sql('SELECT socket, nomeProduto, preco, nota  FROM CPU-Pichau', engine)

socket = []
for dado in product['socket'].dropna():
    socket.append(dado)
nameP = []
for dado in product['tipoProduto'].dropna():
    nameP.append(dado)

precoP = []
for dado in product['preco'].dropna():
    precoP.append(dado)

p = {'Socket: ': socket, 'Tipo de produto': nameP, 'preco': precoP}

comp = pd.DataFrame(data=p)
comp
print(comp)
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