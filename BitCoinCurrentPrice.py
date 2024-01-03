import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

print("Getting the current price of BitCoin...")
response = requests.get(url)

if(response.status_code == 200):
    print(response.json()['time']['updated'])
    print("$" + response.json()['bpi']['USD']['rate'])
else:
    print("Could not get data. Status code: " + str(response.status_code))
