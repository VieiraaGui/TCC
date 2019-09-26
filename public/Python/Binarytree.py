import numpy as np
import pandas as pd
from sklearn import tree

PATH = "C:\User\Teste"
product = pd = pd.read_csv(PATH, delimiter=";")

socket = []
for dado in product['socket'].dropna():
    socket.append(dado)
nameP = []
for dado in product['tipoProduto'].dropna():
    nameP.append(dado)

p = {'Socket: ': socket, 'Tipo de produto': nameP}

comp = pd.DataFrame(data=p)

# Testando a árvore
features = list(comp.columns[1:2])
testTree = comp[features]

result = clf.predict(testTree)

i = 0


def verificaSocket(r):
    if r[1] == 'AM4':
        return "Socket AMD"
    elif r[2] == '1151' or r[2] == '1151 v2':
        return "Socket Intel"


for resp in result:
    print(str(product[i]) + '-' + verificaSocket(resp))