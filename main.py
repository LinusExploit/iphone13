# This is a sample Python script that checks the availability of iphone 13 in UAE.
import requests
import urllib3
import json
import sys
import time
url ='https://reserve-prime.apple.com/AE/en_AE/reserve/A/availability?iPP=N'
availability_url = 'https://reserve-prime.apple.com/AE/en_AE/reserve/A/availability.json'
products = {}
parts = [
    {
        "partNumber": "MLVH3AA/A",
        "description": "iPhone 13 Pro 512GB Graphite",
        "color": "Graphite",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLVE3AA/A",
        "description": "iPhone 13 Pro 256GB Graphite",
        "color": "Graphite",
        "capacity": "256GB",
        "screenSize": '6.1-inch display<sup>1<\/sup>',

    },
    {
        "partNumber": "MLL73AA/A",
        "description": "iPhone 13 Pro Max 128GB Silver",
        "color": "Silver",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLVK3AA/A",
        "description": "iPhone 13 Pro 256GB Gold",
        "color": "Gold",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLVQ3AA/A",
        "description": "iPhone 13 Pro 512GB Gold",
        "color": "Gold",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLLF3AA/A",
        "description": "iPhone 13 Pro Max 512GB Graphite",
        "color": "Graphite",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLV93AA/A",
        "description": "iPhone 13 Pro 128GB Graphite",
        "color": "Graphite",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLLJ3AA/A",
        "description": "iPhone 13 Pro Max 512GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLLA3AA/A",
        "description": "iPhone 13 Pro Max 256GB Graphite",
        "color": "Graphite",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLVU3AA/A",
        "description": "iPhone 13 Pro 512GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLLM3AA/A",
        "description": "iPhone 13 Pro Max 1TB Gold",
        "color": "Gold",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLW03AA/A",
        "description": "iPhone 13 Pro 1TB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLL93AA/A",
        "description": "iPhone 13 Pro Max 128GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLVW3AA/A",
        "description": "iPhone 13 Pro 1TB Silver",
        "color": "Silver",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLL63AA/A",
        "description": "iPhone 13 Pro Max 128GB Graphite",
        "color": "Graphite",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLLC3AA/A",
        "description": "iPhone 13 Pro Max 256GB Silver",
        "color": "Silver",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLLK3AA/A",
        "description": "iPhone 13 Pro Max 1TB Graphite",
        "color": "Graphite",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLLH3AA/A",
        "description": "iPhone 13 Pro Max 512GB Gold",
        "color": "Gold",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLVC3AA/A",
        "description": "iPhone 13 Pro 128GB Gold",
        "color": "Gold",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLLE3AA/A",
        "description": "iPhone 13 Pro Max 256GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLVY3AA/A",
        "description": "iPhone 13 Pro 1TB Gold",
        "color": "Gold",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLL83AA/A",
        "description": "iPhone 13 Pro Max 128GB Gold",
        "color": "Gold",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLVP3AA/A",
        "description": "iPhone 13 Pro 256GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "256GB",
        "screenSize": '6.1-inch display<sup>1<\/sup>',

    },
    {
        "partNumber": "MLLN3AA/A",
        "description": "iPhone 13 Pro Max 1TB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLVA3AA/A",
        "description": "iPhone 13 Pro 128GB Silver",
        "color": "Silver",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLVD3AA/A",
        "description": "iPhone 13 Pro 128GB Sierra Blue",
        "color": "Sierra Blue",
        "capacity": "128GB",

    },
    {
        "partNumber": "MLVF3AA/A",
        "description": "iPhone 13 Pro 256GB Silver",
        "color": "Silver",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLLD3AA/A",
        "description": "iPhone 13 Pro Max 256GB Gold",
        "color": "Gold",
        "capacity": "256GB",

    },
    {
        "partNumber": "MLLL3AA/A",
        "description": "iPhone 13 Pro Max 1TB Silver",
        "color": "Silver",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLVV3AA/A",
        "description": "iPhone 13 Pro 1TB Graphite",
        "color": "Graphite",
        "capacity": "1TB",

    },
    {
        "partNumber": "MLLG3AA/A",
        "description": "iPhone 13 Pro Max 512GB Silver",
        "color": "Silver",
        "capacity": "512GB",

    },
    {
        "partNumber": "MLVN3AA/A",
        "description": "iPhone 13 Pro 512GB Silver",
        "color": "Silver",
        "capacity": "512GB",

    },
]


stores = [
    {'storeNumber':'R597',
     'city': 'Dubai',
     'Name': 'Dubai Mall'

    },

    {'storeNumber': 'R596',
     'city': 'Dubai',
     'Name': 'Mall of the emirates',
     },

    {'storeNumber': 'R595',
     'city': 'Abu Dhabi',
     'Name': 'Yas Mall',
     },




]


session = requests.session()
session.verify = False
urllib3.disable_warnings()


def fetch_products():
    response = session.get(url, verify=False)
    p_av = session.get(availability_url)
    #storing all received products inside the products dictionary
    global products
    products =json.loads(p_av.text)['stores']

def any_available():

    for part in parts:
        #print(part)
        for store in stores:
            #print(store)
            if products[store['storeNumber']][part['partNumber']]['availability']['unlocked'] == True:
                print('an Iphone is available Please check the web page')
                print(part)
                sys.exit()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        while(True):

            fetch_products()
            any_available()
            print('We are still checking! Please Hang on there, May be Grab something to Eat!\n')
            time.sleep(5)
