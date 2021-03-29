import csv
import priceTracker as pt
import schedule
import time

def test():
    print('hello')

def checkOffer(fileName='siteList.csv'):
    Offers=[]
    productList=[]

    with open(fileName, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            productList.append(row)

    for product in productList:
        offer=pt.compare(product['URL'] , product['comparingPrice'])
        if offer:
            Offers.append(offer)
    print(Offers)

if __name__=='__main__':
    schedule.every().day.at("20:02").do(checkOffer,'siteList.csv')
    while True:
        schedule.run_pending()