import csv
import priceTracker as pt
import schedule
import datetime



def loadCSV(fileName='siteList.csv'):
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
    if(Offers):
        for offer in Offers:
            print(f"\"{offer['name']}\" is now available for {offer['price']}")
    else:
        print("No good offers....")
    currentTime = datetime.datetime.now()
    print ("Last Updated : ",currentTime.strftime("%Y-%m-%d %H:%M:%S"))

def sendMail():
    pass

if __name__=='__main__':

    # First run
    loadCSV()

    # Schedule setup
    schedule.every().day.at("20:02").do(loadCSV,'siteList.csv')
    while True:
        schedule.run_pending()