import requests
from bs4 import BeautifulSoup
import threading
import csv
import schedule
import time
import datetime

Offers=[]

# User agent Header for requesting page
headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

def stripPrice(elem):
    price = elem.strip()
    price = price[2:-3]
    price = price.replace(',','')
    price = int(price)

    return price

def getDetails(URL):

    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find('span',id='productTitle').text.strip()

    td = soup.find('td', text = 'Price:')
    
    try:
        priceBlock = td.nextSibling.nextSibling.text
        price = stripPrice(priceBlock)
        return name, price
    except:
        print(name)
        print('Product is not available or the link is broken')
    return

    

def compare(URL, targetPrice):
    targetPrice = int(targetPrice.replace(',' , ''))
    
    try:
        productName, sellingPrice = getDetails(URL)
        print(productName, ': ', sellingPrice)

        offer = {'name': productName, 'price': sellingPrice}

        if sellingPrice < targetPrice:
            Offers.append(offer)

    except:
        pass

    return
        

def checkOffers(fileName='siteList.csv'):
    T=[]
    productList=[]
    with open(fileName, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            productList.append(row)
        
    for i in range(len(productList)):
        T.append(threading.Thread(target=compare, args=(productList[i]['URL'] , productList[i]['targetPrice'])))
        T[i].start()

    for i in range(len(T)):
        T[i].join()

    # for product in productList:
    #     compare(product['URL'], product['targetPrice'])

    global Offers
    if(Offers):
        for offer in Offers:
            print(f"\"{offer['name']}\" is now available for {offer['price']}")
    else:
        print("No good offers....")
    currentTime = datetime.datetime.now()
    print ("Last Updated : ", currentTime.strftime("%Y-%m-%d %H:%M:%S"))

    Offers.clear()

def sendMail():
    pass

if __name__=='__main__':

    # First run
    start_time = time.time()
    checkOffers()
    print("---Execution Time: %s seconds ---" % (time.time() - start_time))

    # Schedule setup
    # schedule.every().day.at("20:02").do(checkOffers,'siteList.csv')
    # while True:
    #     schedule.run_pending()