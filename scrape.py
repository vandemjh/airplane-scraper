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
print("Scrape exported to airplane.json")

valueRange = []
for i in range(len(toReturn.values())):
    valueRange.append(i)

sortedValues = list(toReturn.values())
sortedValues.sort(reverse = True)

stopPoint = len(valueRange) // 10

try:
    import matplotlib.pyplot as plt
except:
    print("It doesn't look like you have matplotlib installed\n\tInstall it using \"pip3 install matplotlib\"")
    quit()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(valueRange[0:stopPoint], sortedValues[0:stopPoint])
ax.xlabel("Code fragement")
ax.ylabel("Number of occurance")
ax.title("Number of occurances by code fragement (10% of values)")
plt.show()
