#!/usr/bin/python3

# Logs all html available through terrible airplane wifi
import requests
import json
import os
import math


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
print("Scrape exported to airplane.json")

valueRange = []
for i in range(len(toReturn.values())):
    valueRange.append(i)

sortedValues = list(toReturn.values())
sortedValues.sort(reverse = True)

stopPoint = 100 if len(sortedValues) > 100 else len(sortedValues)# math.floor(len(valueRange) * .1)
stopPercent = 100 / len(sortedValues)

try:
    import matplotlib.pyplot as plt
except:
    print("It doesn't look like you have matplotlib installed\n\tInstall it using \"pip3 install matplotlib\"")
    quit()

fig = plt.figure()
ax = fig.add_axes([.1,.1,.8,.8])
ax.scatter(valueRange[0:stopPoint], sortedValues[0:stopPoint])
ax.set_xlabel("Code fragement")
ax.set_ylabel("Number of occurance")
# plt.suptitle('Number of occurances by code fragement (10% of values)', fontsize = 12)
ax.set_title("Number of occurances by code fragement (" + str("<.1" if math.floor(stopPercent * 100) == 0 else math.floor(stopPercent * 100)) + "% of values)")
# plt.show()
plt.savefig("Number of occurances by code fragement")
plt.close(fig)


fig = plt.figure()
ax = fig.add_axes([.1,.1,.8,.8])
ax.loglog(valueRange, sortedValues)
ax.set_xlabel("Code fragement")
ax.set_ylabel("Number of occurance")
ax.set_title("Log Log Graph of Code fragements by number of occurances")
# plt.show()
plt.savefig("Log Log Graph of Code fragements by number of occurances")
plt.close(fig)
