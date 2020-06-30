#!/usr/bin/env python3

import requests
import datetime
response = requests.get("http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    print("Status Error")

jsonData = response.json()

issLocation = jsonData["timestamp"]

issTimestamp = datetime.datetime.fromtimestamp(issLocation).strftime('%c')

print(issTimestamp) 


print(response.json())

