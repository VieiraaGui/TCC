import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mydb = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database='baseteste'
)

mycursor = mydb.cursor()
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome("C:\Selenium\chromedriver", options=options)
driver.set_window_position(540, 0)
cpuArray = []

class Cpu:
    def __init__(self, name, price, availability, socket, store):
        self.name = name
        self.price = price.replace('.','')
        self.availability = availability
        self.socket = socket
        self.store = store

    def printCPU(product):
        print('Produto: %s \nPreço: R$%s \nDisponibilidade: %s \nSocket: %s \nLoja: %s' % (
        product.name, product.price, product.availability, product.socket, product.store))

def buscaProduto(linkProduto, name, socket, store):
    driver.get(linkProduto)
    preco = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[2]/span[2]/span').text
    if len(preco) < 10:
        preco = driver.find_element_by_xpath(
            '//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[2]/span[1]/span[2]/span').text
    preco = preco[10:len(preco) - 3]
    disponibilidade = driver.find_element_by_xpath(
        '//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[1]/div[1]/span').text
    disponibilidade = disponibilidade[8:len(disponibilidade)]
    name = Cpu(name, preco, disponibilidade, socket, store)
    cpuArray.append(name)

########## AMD ##########
buscaProduto('https://www.pichau.com.br/processador-amd-athlon-200ge-dual-core-3-2ghz-4mb-cache-am4-yd200gc6fbbox','Athlon 200GE', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-athlon-220ge-dual-core-3-4ghz-5mb-cache-am4-yd220gc6fbbox', 'Athlon 220GE', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-athlon-240ge-dual-core-3-5ghz-5mb-cache-am4-yd240gc6fbbox', 'Athlon 240GE', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-3-1200-quad-core-3-1ghz-3-4ghz-turbo-10mb-cache-am4-yd1200bbaebox','Ryzen 3 1200', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-3-1300x-quad-core-3-5ghz-3-7ghz-turbo-10mb-cache-am4-yd130xbbaebox','Ryzen 3 1300X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-3-2200g-quad-core-3-5ghz-3-7ghz-turbo-6mb-cache-am4-yd2200c5fbbox','Ryzen 3 2200G', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-3-3200g-quad-core-3-6ghz-4ghz-turbo-6mb-cache-am4-yd3200c5fhbox','Ryzen 3 3200G', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-1400-quad-core-3-2ghz-3-4ghz-turbo-10mb-cache-am4-yd1400bbaebox','Ryzen 5 1400', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-1500x-quad-core-3-5ghz-3-7ghz-turbo-18mb-cache-am4-yd150xbbaebox','Ryzen 5 1500', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-1500x-quad-core-3-5ghz-3-7ghz-turbo-18mb-cache-am4-yd150xbbaebox', 'Ryzen 5 1500X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-1600-hexa-core-3-2ghz-3-6ghz-turbo-19mb-cache-am4-yd1600bbaebox','Ryzen 5 1600', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-1600x-hexa-core-3-6ghz-4ghz-turbo-19mb-cache-am4-yd160xbcaewof','Ryzen 5 1600X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-2400g-quad-core-3-6ghz-3-9ghz-turbo-6mb-cache-am4-yd2400c5fbbox','Ryzen 5 2400G', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-3400g-quad-core-3-7ghz-4-2ghz-turbo-6mb-cache-am4-yd3400c5fhbox','Ryzen 5 3400G', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-2600-hexa-core-3-4ghz-3-9ghz-turbo-19mb-cache-am4-yd2600bbafbox','Ryzen 5 2600', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-2600x-hexa-core-3-6ghz-4-2ghz-turbo-19mb-cache-am4-yd260xbcafbox','Ryzen 5 2600X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-3600-hexa-core-3-6ghz-4-2ghz-turbo-35mb-cache-am4-yd3600bbafbox','Ryzen 5 3600', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-5-3600x-hexa-core-3-8ghz-4-4ghz-turbo-35mb-cache-am4-yd360xbbafbox','Ryzen 5 3600X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-1700-octa-core-3ghz-3-7ghz-turbo-20mb-cache-am4-yd1700bbaebox','Ryzen 7 1700', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-1700x-octa-core-3-4ghz-3-8ghz-turbo-20mb-cache-am4-yd170xbcaewof','Ryzen 7 1700X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-1800x-octa-core-3-6ghz-4ghz-turbo-20mb-cache-am4-yd180xbcaewof','Ryzen 7 1800X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-2700x-octa-core-3-7ghz-4-3ghz-turbo-20mb-cache-am4-yd270xbgafbox','Ryzen 7 2700X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-3700x-octa-core-3-6ghz-4-4ghz-turbo-36mb-cache-am4-yd370xbgafbox', 'Ryzen 7 3700', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-7-3800x-octa-core-3-9ghz-4-5ghz-turbo-36mb-cache-am4','Ryzen 7 3800X', 'AM4', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-amd-ryzen-9-3900x-12-cores-3-8ghz-4-6ghz-turbo-70mb-cache-am4','Ryzen 9 3900X', 'AM4', 'Pichau')
########## Intel ##########
buscaProduto('https://www.pichau.com.br/processador-intel-pentium-gold-g5400-dual-core-3-7ghz-4mb-cache-lga1151-bx80684g5400', 'Pentium G5400', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i3-8100-quad-core-3-6ghz-6mb-cache-lga1151-bx80684i38100', 'i3 8100', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i3-8300-quad-core-3-7ghz-8mb-cache-lga1151-bx80684i38300', 'i3 8300', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i3-8350k-quad-core-4ghz-8mb-cache-lga1151-bx80684i38350k', 'i3 8350K', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i3-9100-quad-core-3-6ghz-4-2ghz-turbo-6mb-cache-lga1151-bx80684i39100f', 'i3 9100', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-8400-hexa-core-2-8ghz-4ghz-turbo-9mb-cache-lga1151-bx80684i58400', 'i5 8400', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-8500-hexa-core-3ghz-4-1ghz-turbo-9mb-cache-lga1151-bx80684i58500', 'i5 8500', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-8600-hexa-core-3-1ghz-4-3ghz-turbo-9mb-cache-lga1151-bx80684i58600', 'i5 8600', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-8600k-hexa-core-3-6ghz-4-3ghz-turbo-9mb-cache-lga1151-bx80684i58600k', 'i5 8600K', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-9400f-hexa-core-2-9ghz-4-1ghz-turbo-9mb-cache-lga1151-bx80684i59400f', 'i5 9400F', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-9600kf-hexa-core-3-7ghz-4-6ghz-turbo-9mb-cache-lga1151-bx80684i59600kf', 'i5 9600KF', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i5-9600k-hexa-core-3-7ghz-4-6ghz-turbo-9mb-cache-lga1151-bx80684i59600k', 'i5 9600K', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i7-8700-hexa-core-3-2ghz-4-6ghz-turbo-12mb-cache-lga1151-bx80684i78700', 'i7 8700', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i7-8700k-hexa-core-3-7ghz-4-7ghz-turbo-12mb-cache-lga1151-bx80684i78700k', 'i7 8700K', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i7-9700kf-octa-core-3-6ghz-4-9ghz-turbo-12mb-cache-lga1151-bx80684i79700kf', 'i7 9700KF', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i7-9700k-octa-core-3-6ghz-4-9ghz-turbo-12mb-cache-lga1151-bx80684i79700kf', 'i7 9700K', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i9-9900kf-octa-core-3-6ghz-5ghz-turbo-24mb-cache-lga1151-bx80684i99900kf', 'i9 9900KF', '1151 v2', 'Pichau')
buscaProduto('https://www.pichau.com.br/processador-intel-core-i9-9900k-octa-core-3-6ghz-5ghz-turbo-16mb-cache-lga1151-bx80684i99900k', 'i9 9900K', '1151 v2', 'Pichau')

# for i in range(len(cpuArray)):
#     print('%s %s%s %s %s %s' % (cpuArray[i].name, 'R$', cpuArray[i].price, cpuArray[i].socket, cpuArray[i].availability, cpuArray[i].store))

try:
    for i in range(len(cpuArray)):
        mycursor.execute('INSERT INTO CPU (cpuName, cpuPrice, cpuSocket, cpuAvailability, store) VALUES (' + '\'' + cpuArray[i].name + '\'' + ',' + '\'' + cpuArray[i].price + '\'' + ',' + '\'' + cpuArray[i].socket + '\'' + ',' + '\'' + cpuArray[i].availability + '\''  + ',' + '\'' + cpuArray[i].store + '\'' + ')')
        print('Dados inseridos no banco de dados com sucesso!')
except:
    print("A inserção de dados falhou.")

mydb.commit()
mydb.close

