import os

import numpy as np
import pandas as pd
from sklearn import tree
import graphviz
import mysql.connector
from sqlalchemy import create_engine

pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_rows', 1000)
mydb = mysql.connector.connect(
    user="root",
    password="",
    host="34.95.209.0",
    database='dados'
)

dataCpu = pd.read_sql('select cpuName, cpuPrice, cpuSocket, store, cpuScore from CPU where cpuAvailability  = '
                      '"DISPONIVEL"', mydb)
i = 0
# Inicia CPU
socketCpu = []
for dado in dataCpu['cpuSocket'].dropna():
    socketCpu.append(dado)

nameCpu = []
for dado in dataCpu['cpuName'].dropna():
    nameCpu.append(dado)

precoCpu = []
for dado in dataCpu['cpuPrice'].dropna():
    precoCpu.append(dado)

notaCpu = []
for dado in dataCpu['cpuScore'].dropna():
    notaCpu.append(dado)
desemp = []
if notaCpu[i] <= 40 and precoCpu[i] < 500:
    desemp.append('Razoavel')

lojaCpu = []
for dado in dataCpu['store'].dropna():
    lojaCpu.append(dado)

cpu = {'Processador': nameCpu, 'Preço': precoCpu, 'Socket': socketCpu, 'Nota': notaCpu, 'Loja': lojaCpu}
processador = pd.DataFrame(data=cpu)

# Inicia GPU
dataGpu = pd.read_sql(
    'select gpuName, gpuModel, gpuPrice, gpuVRAM, store, gpuScore from GPU where gpuAvailability = "DISPONIVEL"', mydb)

gpuName = []
for dado in dataGpu['gpuName'].dropna():
    gpuName.append(dado)

gpuModel = []
for dado in dataGpu['gpuName'].dropna():
    gpuModel.append(dado)

gpuRam = []
for dado in dataGpu['gpuVRAM'].dropna():
    gpuRam.append(dado)

gpuPrice = []
for dado in dataGpu['gpuPrice'].dropna():
    gpuPrice.append(dado)

gpuScore = []
for dado in dataGpu['gpuScore'].dropna():
    gpuScore.append(dado)

gpuStore = []
for dado in dataGpu['store'].dropna():
    gpuStore.append(dado)

placaV = {'Placa Mãe': gpuName, 'Modelo': gpuModel, 'Memória': gpuRam, 'Nota': gpuScore, 'Loja': gpuStore}
placaVi = pd.DataFrame(data=cpu)

# Inicia MOBO

dataMobo = pd.read_sql('select moboModel, moboSocket, moboPrice, store from MOBO where moboAvailability = "DISPONIVEL"',
                       mydb)

socketMobo = []
for dado in dataMobo['moboSocket'].dropna():
    socketMobo.append(dado)

nameMobo = []
for dado in dataMobo['moboModel'].dropna():
    nameMobo.append(dado)

priceMobo = []
for dado in dataMobo['moboPrice'].dropna():
    priceMobo.append(dado)

storeMobo = []
for dado in dataMobo['store'].dropna():
    storeMobo.append(dado)

placaMae = {'Placa Mãe': nameMobo, 'Socket': socketMobo, 'Preço': priceMobo, 'Loja': storeMobo}
placaM = pd.DataFrame(data=placaMae)

# Inicia Ram
dataRam = pd.read_sql('select ramName, ramPrice, ramSize, ramAvailability, store from RAM where  ramAvailability = '
                      '"DISPONIVEl"', mydb)

ramName = []
for dado in dataRam['ramName'].dropna():
    ramName.append(dado)

ramSize = []
for dado in dataRam['ramSize'].dropna():
    ramSize.append(dado)

ramPrice = []
for dado in dataRam['ramPrice'].dropna():
    ramPrice.append(dado)

ramStore = []
for dado in dataRam['store'].dropna():
    ramStore.append(dado)

memRam = {'Nome_Ram': ramName, 'Tamanho': ramSize, 'Preco': ramPrice, 'Loja': ramStore}
ram = pd.DataFrame(data=memRam)

comp = pd.concat([processador[nameCpu, notaCpu, precoCpu], placaVi[gpuName, gpuScore, gpuPrice, gpuStore],
                  placaM[nameMobo, priceMobo, storeMobo], ram[ramSize, ramPrice, ramStore]], axis=1)

print(comp)

utilidade = []

for nota in comp['Nota']:
    for desemp1 in comp['Desempenho']:
        desemp = True
        if nota <= 20 and desemp1 == 'Razoavel':
            utilidade.append('Profissional')
        if nota <= 40 and desemp1 == 'Razoavel':
            utilidade.append('Profissional')
        if nota <= 60 and desemp1 == 'Bom':
            utilidade.append('Games')
        if nota >= 61 and desemp1 == 'Excelente':
            utilidade.append('Games')

u = {'Utilidade': utilidade}

utilidadeFinal = pd.DataFrame(data=u)

dataframe = pd.concat([comp, utilidadeFinal], axis=1)

# testando a árvore de decisão

features = list(dataframe.columns[1:6])
X = dataframe = [features]

target = list(dataframe.columns[6:8])
y = dataframe = [target]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# ###############################################
