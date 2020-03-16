#!/usr/bin/python3

# Logs all html available through terrible airplane wifi
import requests
import json


# airplane = open("airplane.json","w")

# toReturn = {}
# for i in range(100):
#     URL = "https://www.aainflight.com/media/" + str(i)
#     page = requests.get(URL)
#     if (page.status_code == 200):
#         contentSplit = str(page.content).split()
#         for word in contentSplit:
#             # This is hacky
#             for inWord in word.split("\n"):
#                 for inInWord in inWord.split("\t"):
#                     if not word in toReturn:
#                         toReturn[inInWord] = 1
#                     else:
#                         toReturn[inInWord] += 1

toReturn = json.loads(open("airplane.json","r").read())

largestVal = 0
for val in toReturn.values():
    if (val > largestVal):
        largestVal = val

# json.dump(toReturn, airplane)

valueRange = []
for i in range(len(toReturn.values())):
    valueRange.append(i)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(valueRange, toReturn.values(), color = 'r')
ax.set_xlabel("Code fragement")
ax.set_ylabel("Number of occurance")
ax.set_title("Number of occurances by code fragement")
plt.show()
