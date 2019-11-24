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

dataCpu = pd.read_sql('select cpuName, cpuPrice, cpuSocket, store, from CPU where cpuAvailability  = "DISPONIVEL"', mydb)

#Inicia CPU
socketCpu = []
for dado in dataCpu['cpuSocket'].dropna():
    socketCpu.append(dado)

nameCpu = []
for dado in dataCpu['cpuName'].dropna():
    nameCpu.append(dado)

precoCpu = []
for dado in dataCpu['cpuPrice'].dropna():
    precoCpu.append(dado)

lojaCpu = []
for dado in dataCpu['store'].dropna():
    lojaCpu.append(dado)

dispCpu = []
for dado in dataCpu['cpuAvailability'].dropna():
    dispCpu.append(dado)

cpu = {'Processador': nameCpu, 'Preço': precoCpu, 'Socket': socketCpu, 'Loja': lojaCpu}
processador = pd.DataFrame(data=cpu)

#Inicia GPU
dataGpu = pd.read_sql('select gpuName, gpuModel, gpuPrice, gpuVRAM, store from GPU where gpuAvailability = "DISPONIVEL"', mydb)

gpuName = []
for dado in dataGpu['gpuName'].dropna():
    gpuName.append(dado)

gpuModel = []
for dado in dataGpu['gpuName'].dropna():
    gpuModel.append(dado)

gpuPrice = []
for dado in dataGpu['gpuPrice'].dropna():
    gpuPrice.append(dado)

gpuStore = []
for dado in dataGpu['store'].dropna():
    gpuStore.append(dado)
cpu = {'P': nameCpu, 'Preço |': precoCpu, 'Socket |': socketCpu, 'Loja |': lojaCpu, 'Situação |': dispCpu}
processador = pd.DataFrame(data=cpu)

#Inicia MOBO

dataMobo = pd.read_sql('select moboModel, moboSocket, moboPrice, store from MOBO where moboAvailability = "DISPONIVEL"', mydb)

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
mobo = pd.DataFrame(data=placaMae)

#Inicia Ram
dataRam = pd.read_sql('select ramName, ramPrice, ramSize, ramAvailability, store from RAM where  ramAvailability = '
                      '"DISPONIVEl"', mydb)

ramName = []
for dado in dataCpu['ramName'].dropna():
    ramName.append(dado)

ramSize = []
for dado in dataCpu['ramSize'].dropna():
    ramSize.append(dado)

ramPrice = []
for dado in dataCpu['ramPrice'].dropna():
    ramPrice.append(dado)

ramStore = []
for dado in dataCpu['store'].dropna():
    ramStore.append(dado)

memRam = {'Nome Ram': ramName, 'Tamanho': ramSize, 'Preço': ramPrice, 'Loja': ramStore}
ram = pd.DataFrame(data=memRam)



###############################################






