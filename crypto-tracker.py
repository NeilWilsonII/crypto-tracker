from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time
import io
import lxml

def getCoin(coinName, buyIn, quantity):
    url='https://coinmarketcap.com/currencies/{0}/'.format(coinName)

    content = requests.get(url).text
    soup = BeautifulSoup(content, "lxml")
    #print(soup.prettify())

    print(coinName)

    content2 = json.dumps(content)
    #print(content2)
    #print("------------------------------------------------------------")
    #print("------------------------------------------------------------")
    #print("------------------------------------------------------------")
    #print("------------------------------------------------------------")

    mydivs = soup.findAll("div", {"priceValue___11gHJ"})
    #print(mydivs)
    mydivs2 = str(mydivs)
    mydivlen = len(mydivs2)
    #print(mydivs2)
    coinPrice = mydivs2[34:-7]
    print(coinPrice)

    totalCurrentValue = float(coinPrice) * float(quantity)
    print(totalCurrentValue)

    buyValue = float(buyIn) * float(quantity)

    percent = totalCurrentValue/buyValue
    percentUp = round((1-percent)*(-100), 2)
    precentSymbol = (str(percentUp), "%")

    print(percentUp)
    return(buyValue, totalCurrentValue)


#1.26 1.43 1.0321 
algo = getCoin("Algorand", 1.24, 284.104)

print("------------------------------------------------------------")
print("------------------------------------------------------------")
district = getCoin("district0x", .2712, 177.30245)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
chain = getCoin("chainlink", 30.31, 6.499847)
print("------------------------------------------------------------")
print("------------------------------------------------------------")

totalBuyValue = (algo[0] + district[0] + chain[0])
totalCurrentValue = (algo[1] + district[1] + chain[1])

MoneyUp = totalCurrentValue - totalBuyValue

print(MoneyUp)