import requests
from bs4 import BeautifulSoup

#My user agent 
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
URL='https://www.amazon.in/Bar-1700D-Bluetooth-Connectivity-Entertainment/dp/B08C6G66SR/ref=sr_1_1?_encoding=UTF8&dchild=1&m=A14CZOWI0VEHLG&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_r=KMY1YX7Q3V3NWGY71T56&pf_rd_t=36701&qid=1617005616&refinements=p_6%3AA14CZOWI0VEHLG%2Cp_89%3ABoat%7CEDICT&rnid=3837712031&s=electronics&smid=A14CZOWI0VEHLG&sr=1-1'

def getPrice(URL,headers):
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    td = soup.find('td', text='M.R.P.:')
    table=td.parent.parent
    rows=table.find_all('tr')

    price=stripPrice(rows)   

    return price

def stripPrice(elem):
    price = elem[1].find('span').get_text().strip()
    price=price[2:-3]
    price=price.replace(',','')
    price=int(price)
    
    return price

def compare(URL,headers,price):
    sale=int(getPrice(URL,headers))
    if sale<price:
        print('True')
    else:
        print('False')

print(getPrice(URL,headers))