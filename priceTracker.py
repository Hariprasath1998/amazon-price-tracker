import requests
from bs4 import BeautifulSoup

#My user agent - Add Yours here
file = open('myUserAgent.txt','r')
myUserAgent = file.readline()

# User agent Header for requesting page
headers={'User-Agent' : myUserAgent}

def fetchPage(URL):
    page = requests.get(URL,headers=headers)
    return BeautifulSoup(page.content,'html.parser')

def stripPrice(elem):
    price = elem[1].find('span').get_text().strip()
    price = price[2:-3]
    price = price.replace(',','')
    price = int(price)

    return price

def getPrice(URL):
    soup = fetchPage(URL)
    
    name = soup.find('span',id='productTitle').text.strip()

    td = soup.find('td', text = 'M.R.P.:')
    table = td.parent.parent
    rows = table.find_all('tr')

    price=stripPrice(rows)
    product={'name' : name,'price' : price}

    return product

def compare(URL,price):
    price=int(price)
    sale = getPrice(URL)
    if sale['price'] < price:
        return sale
    else:
        return False
