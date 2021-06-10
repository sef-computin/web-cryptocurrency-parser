# link = 'https://coinmarketcap.com/all/views/all/'

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

def get_html(url):
    r = requests.get(url)   #Respond
    return r.text           #Возвращает html код

def get_all_names(html):
    soup = BeautifulSoup(html,"lxml")
    namesoup = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    pricesoup = soup.find('table', id='currencies-all').find_all('td',class_='no-wrap text-right')
    names = []
    prices = []
    for name in namesoup:
        try:
            text = name.find('a', class_='currency-name-container').contents[0]
        except: text = ''
        names.append(text)
    for price in pricesoup:
        try:
            usd = price.find('a', class_='price').get('data-usd')
            prices.append(usd)
        except: usd=''
    data = {'names': names,
            'prices': prices}
    return data

def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)
        for i in range(len(data['names'])):
            writer.writerow((data['names'][i], data['prices'][i]))
        print(len(data['names']), " items are parsed")

def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all/'
    html = get_html(url)
    data = get_all_names(html)
    write_csv(data)
    end = datetime.now()
    total = end - start
    print('ended in', str(total))

if __name__ == '__main__':
    main()