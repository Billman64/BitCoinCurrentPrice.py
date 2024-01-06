import requests
import json
import sys


# defaults
verbosity = True
url_base = "https://api.coindesk.com/v1/bpi/"
url = url_base + "currentprice.json"
url_alt = "currentprice/"
#url = "https://api.coindesk.com/v1/bpi/currentprice.json"
curr_list = ["amd","ang","ars","awg","aud","bam","bbd","bdt","bgn","bwp","bzd","chf", "clp",
             "cny", "cad", "cop", "crc", "cuc", "cup","cve","czk", "hkd", "hnl", "hrk", "htg", "huf", "inr","iqd","isk", "jpy", "krw", "kyd", "mxn", "nok", "nzd", "pab", "pen", "qar", "ron", "rub", "sek", "uah", "xas", "xau", "xbt", "xcd", "xdr"]

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
    if (i in curr_list):
        sym=""
        curr = i.upper()
        url = url_base + url_alt + i.upper() + ".json"


# Get the data from the web API
p("Getting the current price of BitCoin...")
response = requests.get(url)

# Output - parsing data
if(response.status_code == 200):
    p(response.json()['time']['updated'])
    print(sym + response.json()['bpi'][curr]['rate'] + " " + response.json()['bpi'][curr]['description'])
    p("\n" + response.json()['disclaimer'])
else:
    p("Could not get data. Status code: " + str(response.status_code))


