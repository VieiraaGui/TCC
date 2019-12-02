import os

import numpy as np
import pandas as pd
from sklearn import tree
import graphviz
import mysql.connector
from sqlalchemy import create_engine

pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)

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
precoCpu = list(map(int, precoCpu))

notaCpu = []
for dado in dataCpu['cpuScore'].dropna():
    notaCpu.append(dado)

notaCpu = list(map(int, notaCpu))

desemp = []
for i in range(len(notaCpu)):
    if notaCpu[i] <= 50 and precoCpu[i] < 500:
        desemp.append('Razoavel')
    elif notaCpu[i] < 70 and precoCpu[i] <= 1500:
        desemp.append('Bom')
    elif notaCpu[i] >= 70 and precoCpu[i] < 3500:
        desemp.append('Excelente')
    else:
        print(nameCpu[i], notaCpu[i], precoCpu[i])

lojaCpu = []
for dado in dataCpu['store'].dropna():
    lojaCpu.append(dado)

cpu = {'Processador': nameCpu, 'Preço': precoCpu, 'Socket': socketCpu, 'Nota': notaCpu, 'Desempenho': desemp,
       'Loja': lojaCpu}

processador = pd.DataFrame(data=cpu)

# # Inicia GPU
dataGpu = pd.read_sql(
    'select gpuName, gpuModel, gpuPrice, gpuVRAM, store, gpuScore from GPU where gpuAvailability = "DISPONIVEL"', mydb)

gpuName = []
for dado in dataGpu['gpuName'].dropna():
    gpuName.append(dado)

gpuModel = []
for dado in dataGpu['gpuModel'].dropna():
    gpuModel.append(dado)

gpuRam = []
for dado in dataGpu['gpuVRAM'].dropna():
    gpuRam.append(dado)

gpuPrice = []
for dado in dataGpu['gpuPrice'].dropna():
    gpuPrice.append(dado)
gpuPrice = list(map(int, gpuPrice))

gpuScore = []
for dado in dataGpu['gpuScore'].dropna():
    gpuScore.append(dado)
gpuScore = list(map(int, gpuScore))

desemp = []
for i in range(len(gpuScore)):
    if gpuScore[i] <= 50 and gpuPrice[i] < 800:
        desemp.append('Baixo')
    elif gpuScore[i] < 60 and gpuPrice[i] <= 1900:
        desemp.append('Medio Baixo')
    elif gpuScore[i] < 70 and gpuPrice[i] <= 2500:
        desemp.append('Medio')
    elif gpuScore[i] < 80 and gpuPrice[i] <= 4500:
        desemp.append('Medio Alto')
    elif gpuScore[i] >= 80 and gpuPrice[i] <= 100000:
        desemp.append('Alto')
    else:
        print(gpuName[i], gpuScore[i], gpuPrice[i])

gpuStore = []
for dado in dataGpu['store'].dropna():
    gpuStore.append(dado)

placaV = {'Placa Video': gpuName, 'Modelo': gpuModel, 'Memória': gpuRam, 'Nota': gpuScore, 'Desempenho': desemp,
          'Loja': gpuStore}
placaVi = pd.DataFrame(data=placaV)

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
    dado = dado[0:len(dado) - 2]
    ramSize.append(dado)


ramPrice = []
for dado in dataRam['ramPrice'].dropna():
    ramPrice.append(dado)

ramStore = []
for dado in dataRam['store'].dropna():
    ramStore.append(dado)


memRam = {'Nome_Ram': ramName, 'Tamanho': ramSize, 'Preco': ramPrice, 'Loja': ramStore}
ram = pd.DataFrame(data=memRam)


comp = pd.concat([processador, placaVi, placaM, ram], axis=1)


utilidade = []

for i in comp[processador]:
    for gpuScore in comp[placaVi]:
        for desemp in comp['Desempenho']:
            desemp = True
            if notaCpu <= 20 and gpuScore and desemp == 'Razoavel':
                utilidade.append('Profissional')
            if notaCpu <= 20 and gpuScore and desemp == 'Razoavel':
                utilidade.append('Profissional')
            if notaCpu <= 20 and gpuScore and desemp == 'Bom':
                utilidade.append('Games')
            if notaCpu <= 20 and gpuScore and desemp == 'Excelente':
                utilidade.append('Games')

u = {'Utilidade': utilidade}

utilidadeFinal = pd.DataFrame(data=u)

print(utilidadeFinal)

# dataframe = pd.concat([comp, utilidadeFinal], axis=1)

# # #
# # # ###############################################
