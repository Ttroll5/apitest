#!/usr/bin/python3

import requests
import json
import os
import time 


while True: 
    t= requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").text
    t = json.loads(t)
    price = int(t["bitcoin"]["usd"])
    os.system(f"notify-send -t 3000 \"The price of BTC is {price}\"")
    time.sleep(5)

