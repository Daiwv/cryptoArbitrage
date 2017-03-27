#####Importing modules#############
import requests
import json
###################################

###Prompt user for what coin to analyse###
instrument = input("Enter a coin: ") #This is the symbol of the crypto coin that you want to find arbitrage opportunities for :D
##########################################

##########Config Variables################
minVol = 200 #Minimum volume (In BTC) an exchange should have to be taken into account by this program
#########################################

################Other declarations##########
lowest = {"market": "No markets :(", "price": 10000000000, "volume": 0}
highest = {"market": "No markets :(", "price": 0, "volume": 0}
exchangeUrls = {'no markets :(':'There are no markets available for this asset :(', 'yobit': 'yobit.net', 'indacoin': 'indacoin.com', 'kuna': 'en.kuna.com.ua', 'bitstamp': 'bitstamp.net', 'btc-e': 'btc-e.com', 'bittrex': 'bittrex.com', 'cex': 'cex.io', 'bleutrade': 'bleutrade.com', 'exmo': 'exmo.com', 'hitbtc': 'hitbtc.com', 'poloniex': 'poloniex.com', 'bitfinex': 'bitfinex.com', 'livecoin': 'livecoin.net', 'c-cex': 'c-cex.com', 'kraken': 'kraken.com'}
############################################

########Geting exchange market list and data for the coin########
output = requests.get("https://api.cryptonator.com/api/full/" + instrument + "-btc")
markets = json.loads(output.content.decode("utf-8"))["ticker"]["markets"]
################################################################

##############Finding the cheapest exchange#####################
for market in markets:
    if market["market"] == "Hitbtc":  ###Hitbit has btc withdrawls disabled
        continue
        
    market["volume"] = float(market["volume"]) * float(market["price"])
    market["price"] = float(market["price"])
    
    if float(market["volume"]) >= minVol:
        if float(market["price"]) < lowest["price"]:
            lowest = market
################################################################
            
##############Finding the most expensive exchange###############
    if float(market["volume"]) >= minVol:
        if float(market["price"]) > highest["price"]:
            highest = market
################################################################
            
################Calculating potential profit###################
profit = highest["price"] / (lowest["price"] / 100) - 100
roundedProfit = round(profit, 3)
################################################################

##########Alerting the user of findings#########################
print("Buy " + instrument + " at " + lowest["market"] + " for " + format(lowest["price"], '.8f') + " BTC \tVolume: " + str(lowest["volume"]) + " BTC\nhttp://" + exchangeUrls[lowest["market"].lower()])
print("Sell " + instrument + " at " + highest["market"] + " for " + format(highest["price"], '.8f') + " BTC \tVolume: " + str(highest["volume"]) + " BTC\nhttp://" + exchangeUrls[highest["market"].lower()])
print(str(roundedProfit) + "% profit")
################################################################
