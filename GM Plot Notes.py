# GM Plotting Notes
from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"
mymap = GoogleMapPlotter(41.923151, -87.638176, 14, apikey=apikey) # 14 is the number of zoom clicks your location is from a view of the entire earth

lats = [41.923151 for x in range(10)]
longs = [-87.638176 - x/100 for x in range(10)]
lats[4] = 41.9

mymap.marker(41.923151, -87.638176) # lat, long
mymap.circle(41.923151, -87.638176, 500, "yellow", ew=10) # lat, long, radius(m), color, edge width
mymap.polygon(lats, longs, "red") # fills in any polygons created by your input points
mymap.plot(lats, longs, "yellow", ew=5) # fills in a line created by any points that you input

with open("Data/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
print(data.pop(0))
lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
mymap.scatter(lats, longs, color="green", marker=False, size=2)

mymap.draw("mymap.html")
