# coding=utf8
import pandas as pd
import mysql.connector

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 50)

mydb = mysql.connector.connect(
    user="root",
    password="",
    host="34.95.209.0",
    database='dados'
)

Arquivo = open(r"C:\Git\TCC\static\Comp.json", "w")

valortotal = 3000

selectedMobo = []
selectedRAM = []
selectedPSU = []
selectedHDD = []
selectedSSD = []
selectedCase = []

if valortotal < 1725:
    print('Valor insuficiente para montagem do equipamento')
elif valortotal > 1725 and valortotal <= 2000:
    selectedRAM.append(
        '4GB, R$119.90, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=79700')
    selectedPSU.append('EVGA 400W, R$171.90, https://www.kabum.com.br/produto/59467/fonte-evga-400w-100-n1-0400-l')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append('N/D')
    selectedCase.append(
        'PCYes Mercury, R$149.90, https://www.pichau.com.br/hardware/gabinete/gabinete-pcyes-mercury-lateral-acrilico-preto-verde-mrcptvd1fca')
    valortotal -= (339.90 + 171.90 + 149.90 + 238.99 + 119.90)
    # print(valortotal)
elif valortotal > 2000 and valortotal <= 2500:
    selectedRAM.append(
        '8GB, R$175.90, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101085')
    selectedPSU.append('EVGA 400W, R$171.90, https://www.kabum.com.br/produto/59467/fonte-evga-400w-100-n1-0400-l')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append('N/D')
    selectedCase.append(
        'PCYes Mercury, R$149.90, https://www.pichau.com.br/hardware/gabinete/gabinete-pcyes-mercury-lateral-acrilico-preto-verde-mrcptvd1fca')
    valortotal -= (339.90 + 171.90 + 149.90 + 238.99 + 175.90)
elif valortotal > 2500 and valortotal <= 3000:
    selectedRAM.append(
        '8GB, R$175.90, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101085')
    selectedPSU.append('EVGA 400W, R$171.90, https://www.kabum.com.br/produto/59467/fonte-evga-400w-100-n1-0400-l')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append(
        'SSD 120GB, R$109.99, https://www.terabyteshop.com.br/produto/12222/ssd-adata-su650-120gb-sata-iii-leitura-520mbs-e-gravacao-450mbs-asu650ss-120gt-r')
    selectedCase.append(
        'PCYes Mercury, R$149.90, https://www.pichau.com.br/hardware/gabinete/gabinete-pcyes-mercury-lateral-acrilico-preto-verde-mrcptvd1fca')
    valortotal -= (339.90 + 171.90 + 149.90 + 238.99 + 109.99 + 175.90)
elif valortotal > 3000 and valortotal <= 3500:
    selectedRAM.append(
        '8GB, R$175.90, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101085')
    selectedPSU.append(
        'Corsair 550W, R$224.90, https://www.terabyteshop.com.br/produto/10608/fonte-corsair-vs-series-vs550-550w-cp-9020171-ww-80-plus-white-pfc-ativo')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append(
        'SSD 120GB, R$109.99, https://www.terabyteshop.com.br/produto/12222/ssd-adata-su650-120gb-sata-iii-leitura-520mbs-e-gravacao-450mbs-asu650ss-120gt-r')
    selectedCase.append(
        'PCYes Mercury, R$149.90, https://www.pichau.com.br/hardware/gabinete/gabinete-pcyes-mercury-lateral-acrilico-preto-verde-mrcptvd1fca')
    valortotal -= (339.90 + 224.90 + 149.90 + 238.99 + 109.99 + 175.90)
elif valortotal > 3500 and valortotal < 4000:
    selectedRAM.append(
        '2x8GB, R$351.80, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101085')
    selectedPSU.append(
        'Corsair 550W, R$224.90, https://www.terabyteshop.com.br/produto/10608/fonte-corsair-vs-series-vs550-550w-cp-9020171-ww-80-plus-white-pfc-ativo')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append(
        'SSD 120GB, R$109.99, https://www.terabyteshop.com.br/produto/12222/ssd-adata-su650-120gb-sata-iii-leitura-520mbs-e-gravacao-450mbs-asu650ss-120gt-r')
    selectedCase.append(
        'DeepCool Materxx 50, R$279.00, https://www.terabyteshop.com.br/produto/12220/gabinete-gamer-deepcool-matrexx-50-rgb-3f-mid-tower-black-s-fonte-dp-atx-matrexx50-ar-3f-us')
    valortotal -= (339.90 + 224.90 + 279.00 + 238.99 + 109.99 + (175.90 * 2))
elif valortotal > 4000:
    selectedRAM.append(
        '2x8GB, R$351.80, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101085')
    selectedPSU.append(
        'Corsair 550W, R$224.90, https://www.terabyteshop.com.br/produto/10608/fonte-corsair-vs-series-vs550-550w-cp-9020171-ww-80-plus-white-pfc-ativo')
    selectedHDD.append(
        'HD 1TB, R$238.99, https://www.pichau.com.br/hardware/hard-disk-e-ssd/hd-seagate-1tb-barracuda-3-5-7200-rpm-64mb-cache-sata-iii-st1000dm010')
    selectedSSD.append(
        'SSD 120GB, R$109.99, https://www.terabyteshop.com.br/produto/12222/ssd-adata-su650-120gb-sata-iii-leitura-520mbs-e-gravacao-450mbs-asu650ss-120gt-r')
    selectedCase.append(
        'DeepCool Materxx 50, R$279.00, https://www.terabyteshop.com.br/produto/12220/gabinete-gamer-deepcool-matrexx-50-rgb-3f-mid-tower-black-s-fonte-dp-atx-matrexx50-ar-3f-us')
    valortotal -= (339.90 + 224.90 + 279.00 + 238.99 + 109.99 + (175.90 * 2))

dataCpu = pd.read_sql(
    'SELECT cpuName, cpuPrice, cpuSocket, store, cpuSerial, cpuScore, cpuLink FROM CPU WHERE cpuAvailability  = '
    '"DISPONIVEL" ORDER BY cpuPrice', mydb)

i = 0

# Inicia CPU
socketCpu = []
for dado in dataCpu['cpuSocket'].dropna():
    socketCpu.append(dado)

linkCpu = []
for dado in dataCpu['cpuLink'].dropna():
    linkCpu.append(dado)

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

serialCpu = []
for dado in dataCpu['cpuSerial'].dropna():
    serialCpu.append(dado)

notaCpu = list(map(int, notaCpu))

desemp = []
for i in range(len(notaCpu)):
    if notaCpu[i] <= 50 and precoCpu[i] < 500:
        desemp.append('Razoavel')
    elif notaCpu[i] < 70 and precoCpu[i] <= 1700:
        desemp.append('Bom')
    elif notaCpu[i] >= 70 and precoCpu[i] < 3500:
        desemp.append('Excelente')
    else:
        print(nameCpu[i], notaCpu[i], precoCpu[i])

lojaCpu = []
for dado in dataCpu['store'].dropna():
    lojaCpu.append(dado)

cpu = {'Processador': nameCpu, 'Preço': precoCpu, 'Socket': socketCpu, 'Nota': notaCpu, 'SerialCPU': serialCpu,
       'Desempenho': desemp, 'Loja': lojaCpu, "LinkCPU": linkCpu}

processador = pd.DataFrame(data=cpu)

# # Inicia GPU
dataGpu = pd.read_sql(
    'SELECT gpuName, gpuModel, gpuPrice, gpuVRAM, store, gpuSerial, gpuScore, gpuLink FROM GPU WHERE gpuAvailability = "DISPONIVEL" ORDER BY gpuPrice',
    mydb)

gpuName = []
for dado in dataGpu['gpuName'].dropna():
    gpuName.append(dado)

gpuLink = []
for dado in dataGpu['gpuLink'].dropna():
    gpuLink.append(dado)

gpuModel = []
for dado in dataGpu['gpuModel'].dropna():
    gpuModel.append(dado)

gpuRam = []
for dado in dataGpu['gpuVRAM'].dropna():
    gpuRam.append(dado)

gpuSerial = []
for dado in dataGpu['gpuSerial'].dropna():
    gpuSerial.append(dado)

gpuPrice = []
for dado in dataGpu['gpuPrice'].dropna():
    gpuPrice.append(dado)
gpuPrice = list(map(int, gpuPrice))

gpuScore = []
for dado in dataGpu['gpuScore'].dropna():
    gpuScore.append(dado)
gpuScore = list(map(int, gpuScore))

gpuStore = []
for dado in dataGpu['store'].dropna():
    gpuStore.append(dado)

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

placaV = {'Placa_Video': gpuName, 'Modelo': gpuModel, 'Memória': gpuRam, 'Nota': gpuScore, 'GPUSerial': gpuSerial,
          'Desempenho': desemp,
          'Loja': gpuStore, 'PRECO': gpuPrice, 'GPULink': gpuLink}
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

comp = pd.concat([processador, placaVi], axis=1)

utilidade = []

for i in range(len(processador)):
    for j in range(len(placaVi)):
        if (precoCpu[i] + gpuPrice[j] < valortotal):
            if int(notaCpu[i]) <= 32 and int(gpuScore[j]) <= 31:
                # utilidade.append('0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' + placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                utilidade.append(
                    '0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                        cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                    placaVi['Modelo'][j] + ', R$' + str(placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])
            if int(notaCpu[i]) > 32 and (notaCpu[i]) <= 40 and int(gpuScore[j]) > 31 and int(gpuScore[j]) <= 40.5:
                # utilidade.append('0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' + placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                utilidade.append(
                    '0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                        cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                    placaVi['Modelo'][j] + ', R$' + str(
                        placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])
            if int(notaCpu[i]) > 40 and (notaCpu[i]) <= 67 and int(gpuScore[j]) > 40.5 and int(gpuScore[j]) <= 62.6:
                if (placaVi['Nota'][j] + cpu['Nota'][i]) < 100:
                    # utilidade.append('0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' + placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                    utilidade.append(
                        '0' + str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                            cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                        placaVi['Modelo'][
                            j] + ', R$' + str(placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])
                # utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' +  placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                    cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                                 placaVi['Modelo'][j] + ', R$' + str(
                    placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])
            if int(notaCpu[i]) > 67 and (notaCpu[i]) <= 85 and int(gpuScore[j]) > 62.6 and int(gpuScore[j]) <= 80.7:
                # utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' + placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                    cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                                 placaVi['Modelo'][j] + ', R$' + str(
                    placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])
            if int(notaCpu[i]) > 85 and int(gpuScore[j]) > 80.7:
                # utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['SerialCPU'][i] + ' ' + placaVi['GPUSerial'][j] + ' ' + cpu['Socket'][i])
                utilidade.append(str(placaVi['Nota'][j] + cpu['Nota'][i]) + ' ' + cpu['Processador'][i] + ', R$' + str(
                    cpu['Preço'][i]) + ', ' + cpu['LinkCPU'][i] + '\n' + placaVi['Placa_Video'][j] + ' ' +
                                 placaVi['Modelo'][j] + ', R$' + str(
                    placaVi['PRECO'][j]) + ", " + placaVi['GPULink'][j])

maiorvalor = 0
valori = 0

for i in range(len(utilidade)):
    valor = utilidade[i]
    valor = int(valor[0:3])

    if (maiorvalor < valor):
        maiorvalor = valor
        valori = i

        socket = utilidade[i]
        socket = socket[len(socket) - 3:len(socket)]

# print(utilidade[valori])

if socket == 'AM4':
    selectedMobo.append(
        'GA-AB350M-DS3H V2, R$339.90, https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101715')
else:
    selectedMobo.append(
        'B365M-K, R$329.00, https://www.terabyteshop.com.br/produto/11538/placa-mae-asus-prime-b365m-k-chipset-b365-intel-1151-matx-ddr4')

cpuEgpu = utilidade[valori]
cpuEgpu = cpuEgpu[4:len(cpuEgpu)]
print(cpuEgpu)

print(selectedMobo[0] + '\n' + selectedRAM[0] + '\n' + selectedPSU[0] + '\n' + selectedHDD[0] + '\n' + selectedSSD[
    0] + '\n' + selectedCase[0])

u = {'Utilidade': utilidade}

utilidadeFinal = pd.DataFrame(data=u)

Arquivo.write(
    cpuEgpu + '\n' + selectedMobo[0] + '\n' + selectedRAM[0] + '\n' + selectedPSU[0] + '\n' + selectedHDD[0] + '\n' +
    selectedSSD[0] + '\n' + selectedCase[0])


