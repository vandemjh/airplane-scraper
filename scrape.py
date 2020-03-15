#!/usr/bin/python3

# Logs all html available through terrible airplane wifi
import requests
import json
import reportlab

airplane = open("airplane.json","w")

toReturn = {}
for i in range(1):
    URL = "https://www.aainflight.com/media/" + str(i)
    page = requests.get(URL)
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

largestVal = 0
for val in toReturn.values():
    if (val > largestVal):
        largestVal = val

json.dump(toReturn, airplane, sort_keys=True)

        drawing = Drawing(200, 100)

        data = [
                (13, 5, 20, 22, 37, 45, 19, 4),
                (14, 10, 21, 28, 38, 46, 25, 5)
                ]

        lc = HorizontalLineChart()

        lc.x = 20
        lc.y = 10
        lc.height = 85
        lc.width = 170
        lc.data = data
        lc.lines.symbol = makeMarker('Circle')

        drawing.add(lc)

        return drawing
# chart = ScatterPlot()
# chart.data = toReturn
# chart.width      = 115
# chart.height     = 80
# chart.x          = 30
# chart.y          = 40
# chart.save()
