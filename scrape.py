# Logs all html available through terrible airplane wifi
# Requires requests
import os
import requests
import sys
import json

airplane = open("airplane.json","w")

toReturn = {}
count = 0
for i in range(100):
    URL = "https://www.aainflight.com/media/" + str(i)
    page = requests.get(URL)
    if (page.status_code == 200):
        contentSplit = str(page.content).split()
        for word in contentSplit:
            if not word in toReturn:
                toReturn[word] = 1
            else:
                toReturn[word] += 1

json.dump(toReturn, airplane, sort_keys=True)
