#!/usr/bin/python3

# Logs all html available through terrible airplane wifi
import requests
import json
import os
import math
import re


airplane = open("airplane.json","w")

# Old version of this code, only available while on the flight
# for i in range(100):
#     URL = "https://www.aainflight.com/media/" + str(i)
    # page = requests.get(URL)
    # if (page.status_code == 200):
    #     contentSplit = str(page.content).split()
    #     for word in contentSplit:
    #         # This is hacky
    #         for inWord in word.split("\n"):
    #             for inInWord in inWord.split("\t"):
    #                 if not word in toReturn:
    #                     toReturn[inInWord] = 1
    #                 else:
    #                     toReturn[inInWord] += 1

"""
Finds the URL in the included string
string[string.index("http"):len(string) - 1 - (string[::-1].index("\""))]
  ^          ^        ^          ^        ^          ^             ^
slices       |        |          |        |          |             |
       string from    |          |        |          |             |
               index of "http"   |        |          |             |
                             to length    |          |             |
                                 (index starts at 0) |             |
                                               of reversed         |
                                                         index of last quote
"""
def findURL(string):
    if (isinstance(string, str)):
        return string[string.index("http"):len(string) - 1 - (string[::-1].index("\""))]

"""
Did not add recursion to this on purpose so I would not return all of the internet
"""
def getLinks(URL):
    ALLOW_OUTSIDE_URLS = False
    toReturn = []
    try: # Handles improper links
        page = requests.get(URL)
        if (page.status_code == 200):
            for space in str(page.content).split(" "):
                if (URL in space or ALLOW_OUTSIDE_URLS): # and URL in space for only on this domain
                    newURL = findURL(space)
                    if (newURL != URL): # check for self loops
                        toReturn.append(newURL)
            # for space in str(page.content).split("<a"): # account for anchors
            #     if (URL in space): # and URL in space for only on this domain
            #         toReturn.append(findURL(space))
    except:
        print("Improper link: " + str(URL))
    finally:
        return toReturn
        # return list(filter(lambda x: requests.get(x).status_code == 200, toReturn))
        # Filters out non-links

URL = "https://www.aa.com/"
# print((getLinks(URL)))
allPages = []
for link in getLinks(URL):
    allPages.append(link)
    for link1 in getLinks(link):
        allPages.append(link1)
        # print(getLinks(link1))
        # For more depth, add more loops here

toReturn = {}

for URL in allPages:
    try:
        page = requests.get(URL)
    except: # Handles improper links that have slipped through the cracks
        page.status_code = 500
    if (page.status_code == 200):
        contentSplit = str(page.content).split()
        for word in contentSplit:
            # This is hacky
            for inWord in word.split("\n"):
                for inInWord in inWord.split("\t"):
                    if not word in toReturn:
                        toReturn[inInWord] = 1
                    else:
                        toReturn[inInWord] += 1

json.dump(toReturn, airplane)

airplane.close()
# quit() # Remove later
airplane = open("airplane.json","r")

toReturn = json.loads(airplane.read())

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
sortedKeys = list(toReturn.keys())
sortedValues.sort(reverse = True)

stopPoint = 60 if len(sortedValues) > 60 else len(sortedValues)# math.floor(len(valueRange) * .1)
stopPercent = 60 / len(sortedValues)

try:
    import matplotlib.pyplot as plt
except:
    print("\tIt doesn't look like you have matplotlib installed!\n\tThat's fine, the results of the scrape are exported to file.\n\tYou can also install it using \"pip3 install matplotlib\"")
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

print("Most used code fragement: \"" + str(list(toReturn.keys())[list(toReturn.values()).index(sortedValues[0])]) + "\" used " + str(sortedValues[0]) + " times!")
