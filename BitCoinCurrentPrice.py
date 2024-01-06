import requests
import json
import sys
import os
#from timeit import default_timer as timer

# defaults
verbosity = True
url_base = "https://api.coindesk.com/v1/bpi/"
url = url_base + "currentprice.json"
url_alt = "currentprice/"
#url = "https://api.coindesk.com/v1/bpi/currentprice.json"

curr_list = {"AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYR","BZD","CAD","CDF","CHF","CLF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","FJD","FKP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","STD","STN","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","UYU","UZS","VES","VND","VUV","WST","XAF","XAG","XAU","XBT","XCD","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"}
# converted to a dictionary for (usually) faster read times

def help():
    import os
    print("\n Name: " + os.path.basename(__file__))
    print("\n Description: Gets the current value of BitCoin.")
    print("\n Usage:\n")
    print("\t [q] - Quiet mode. No verbosity, so that only the value is output.")
    print("\t [eur, gbp, usd] - Specify currency.")
    print("\t [v] - Verbose mode. (Default)")
    print("")
    print(" # of currencies supported: " + str(len(curr_list)+3))
    print("Note: Compatible with Python 3.1+. Data source is from Coindesk.")
    print("")
    sys.exit()



def p(str): # simple function that prints only if verbosity allows
    if(verbosity): print(str)

#start = timer()
    
# Get currency, verbosity level from command-line arguments
for i in sys.argv:
    match i.lower():
        case "eur":
            sym = "€"
            curr = "EUR"
        case "gbp":
            sym = "£"
            curr = "GBP"
        case "usd":
            sym = "$"
            curr = "USD"
        case "q":
            verbosity = False
        case "v":
            verbosity = True
        case "h" | "help":
            help()
        case _:
            sym = "$"
            curr = "USD"
    if (i.upper() in curr_list):
        sym=""
        curr = i.upper()
        url = url_base + url_alt + i.upper() + ".json"


# Get the data from the web API
p("Getting the current price of BitCoin...")
response = requests.get(url)

# Output - parsing data
os.system("")
if(response.status_code == 200):
    p(response.json()['time']['updated'])
    print(sym + response.json()['bpi'][curr]['rate'])
    p(response.json()['bpi'][curr]['description'])    
    p("\n" + response.json()['disclaimer'])
else:
    p("Could not get data. Status code: " + str(response.status_code))

#end = timer()
#p("duration (processing): %f ms" %(1000*(end - start))
