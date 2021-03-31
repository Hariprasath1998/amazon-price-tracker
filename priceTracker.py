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
    price = elem.strip()
    price = price[2:-3]
    price = price.replace(',','')
    price = int(price)

    return price

def getPrice(URL):
    soup = fetchPage(URL)
    
    name = soup.find('span',id='productTitle').text.strip()

    td = soup.find('td', text = 'Price:')

    priceBlock=td.nextSibling.nextSibling.text

    price=stripPrice(priceBlock)

    product={'name' : name,'price' : price}

    return product

def compare(URL,price):
    price=int(price.replace(',',''))
    sale = getPrice(URL)
    if sale['price'] < price:
        return sale
    else:
        return False


c = getPrice('https://www.amazon.in/OnePlus-Nord-Gray-256GB-Storage/dp/B08697WT6D/ref=sr_1_2?dchild=1&keywords=oneplus&qid=1617184474&s=electronics&sr=1-2')