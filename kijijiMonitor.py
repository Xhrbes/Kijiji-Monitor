import requests
import json
import time

from datetime import datetime
from bs4 import BeautifulSoup
from pytz import timezone 

url = 'INSERT YOUR OWN KIJIJI LINK TO MONITOR'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

def NewListing(KijijiListing):

    prod_title = KijijiListing[0]
    prod_url = KijijiListing[1]
    prod_url = f'https://www.kijiji.ca{prod_url}'
    prod_image = KijijiListing[2]
    prod_desc = KijijiListing[3] 
    prod_price = KijijiListing[4]
    prod_distance = KijijiListing[5]
    prod_area = KijijiListing[6]
    prod_date = KijijiListing[7]
    tz = timezone('US/Eastern')
    ping_time = datetime.now(tz)
    data = {
        'content': None,
        'embeds': [
            {
                'title': 'New Kijiji Listing!',
                'url': prod_url,
                'color': 7820202,
                'fields': [
                    {
                        'name': prod_title,
                        'value': prod_desc
                    },
                    {
                        'name': 'Listing Details',
                        'value': f'Listing Price - {prod_price}\nListing Area - {prod_area} | {prod_distance} Away From Home.\nPosted - {prod_date}'

                    }
                ],
                'footer': {
                    'text': f'Kijiji Listing Monitor | Developed By Xhrbes#4481| Webhook Posted At [{ping_time}]',
                    'icon_url': 'https://cdn.discordapp.com/avatars/281888279450615808/0d98c33b702cfc5520e3606277e72951.png?size=256'
                },
                'image': {
                    'url': prod_image
                }
            }
        ]
    }
    time.sleep(0.7)
    results = requests.post('INSERT YOUR OWN DISCORD WEBHOOK FOR FUNCTIONALITY', json=data)
    if results.text == '':
        None
    elif results.text != '':
        try:
            results = json.loads(results.text)
            delay = results['retry_after'] / 1000
            if results['message'] == 'You are being rate limited.':
                print(f'Rate Limited, Sleeping [{delay}] Seconds!')
                time.sleep(delay)
                results = requests.post('INSERT YOUR OWN DISCORD WEBHOOK FOR FUNCTIONALITY', json=data)
        except KeyError:
            None

Products = []

def Monitor(count):
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r)
    r.close()
    soup = soup.findAll('div', {'search-item regular-ad'})
    for product in soup:
        product_URL = product['data-vip-url']
        #print(product_URL)
        if product_URL in Products:
            print('ALREADY IN LIST')
            continue
        elif product_URL not in Products:
            if count == 0:
                print('RESTARTING KIJIJI MONITOR!')
                Products.append(product_URL)
            elif count != 0:
                print('DETECTED NEW ITEM!')
                Products.append(product_URL)

                product_image = product.find('img')['data-src']
                #print(product_image)
                product_title = product.find('img')['alt']
                #print(product_title)
                product_price = product.find('div', {'class':'price'}).text
                product_price = product_price.strip()
                #print(product_price)

                product_distance = product.find('div', {'class':'distance'}).text
                product_distance = product_distance.strip()
                #print(product_distance)

                product_date = product.find('span', {'class':'date-posted'}).text
                product_date = product_date.strip()
                #print(product_date)

                product_area = product.find('div', {'class':'location'}).span.text
                product_area = product_area.strip()
                #print(product_area)

                product_desc = product.find('div', {'class':'description'}).text
                product_desc = product_desc.strip()
                ListingDetails = (product_title, product_URL, product_image, product_desc, product_price, product_distance, product_area, product_date)
                NewListing(ListingDetails)
        #print(product_desc)


        #print(Products)

        '''
        print(product_URL)
        print(product_image)
        print(product_title)
        print(product_data)
        print(product_price)
        print(product_distance)
        print(product_date)
        print(product_desc)
        '''
        '''
        
        print(product.find('span', {'class':'date=posted'}))
        print(product.find('div', {'class':'description'}))
        '''
        #time.sleep(1000)


    


def WebScraper():
    print(f'Initializing Monitor!')
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    r.close()
    soup = soup.findAll('div', {'search-item regular-ad'})
    #print(soup[0])
    count = 0
    countv2 = 0
    print('Successfully Connected, Monitoring Kijiji Ad Listings!')
    while True:
        Monitor(count)
        count += 1

WebScraper()
