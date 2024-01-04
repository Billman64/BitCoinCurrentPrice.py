import requests
import json
import sys

# Verbosity/quiet check
verbosity = True
if(sys.argv[1:] and sys.argv[1].lower() == "q"):
    verbosity = False
    
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def p(str):
    if(verbosity): print(str)


p("Getting the current price of BitCoin...")
response = requests.get(url)

if(response.status_code == 200):
    p(response.json()['time']['updated'])
    print("$" + response.json()['bpi']['USD']['rate'])


    
else:
    p("Could not get data. Status code: " + str(response.status_code))


