import requests
import json
import sys


# defaults
verbosity = True
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def p(str): # simple function that prints only if verbosity allows
    if(verbosity): print(str)

# Get currency, verbosity level from command-line arguments
for i in sys.argv:
    match i:
        case "eur":
            sym = "€"
            curr = "EUR"
        case "gbp":
            sym = "£"
            curr = "GBP"
        case "q":
            verbosity = False
        case _:
            sym = "$"
            curr = "USD"

p("Getting the current price of BitCoin...")
response = requests.get(url)

if(response.status_code == 200):
    p(response.json()['time']['updated'])
    print(sym + response.json()['bpi'][curr]['rate'])

else:
    p("Could not get data. Status code: " + str(response.status_code))


