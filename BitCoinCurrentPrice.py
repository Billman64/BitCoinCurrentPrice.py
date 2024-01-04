import requests
import json
import sys


# defaults
verbosity = True
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def help():
    import os
    print("\n Name: " + os.path.basename(__file__))
    print("\n Description: Gets the current value of BitCoin.")
    print("\n Usage:\n")
    print("\t [q] - Quiet mode. No verbosity, so that only the value is output.")
    print("\t [eur, gbp, usd] - Specify currency.")
    print("\t [v] - Verbose mode. (Default)")
    print("")
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

# Get the data from the web API
p("Getting the current price of BitCoin...")
response = requests.get(url)

# Output - parsing data
if(response.status_code == 200):
    p(response.json()['time']['updated'])
    print(sym + response.json()['bpi'][curr]['rate'])
else:
    p("Could not get data. Status code: " + str(response.status_code))


