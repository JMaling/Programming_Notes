# PLOTTING (With matplotlib)
import matplotlib.pyplot as plt  # makes it so that everytime we call it , we can just call it plt
import csv # also can read and work with tab separated values
import numpy as np

plt.figure("TEST A") # creates a new window
plt.plot([1, 2, 3, 4]) # If there is no x axis, just gives index 0, 1, 2 ...
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.figure("TEST B", facecolor="pink") # opens up a new window/figure
x = [x for x in range(11)]
y = [y ** 2 for y in range(11)]
plt.plot(x, y, color="pink", marker=".", markersize=10, linestyle=":", alpha=.5) # takes kwarg (keyword arguments)
# for more information on markers, go to the following link: https://matplotlib.org/api/markers_api.html
plt.xlabel("Number", color="white")
plt.ylabel("Number Squared", color="white")
plt.title("Exponential Graph", color="white", fontsize="20")
plt.axis([0, 11, 0, 110]) # function takes: xmin, xmax, ymin, ymax

# World Firearm Ownership Graphics
with open("Data/World firearms murders and ownership - Sheet 1.tsv") as w:
    reader = csv.reader(w, delimiter="\t") # treats the tabs as commas, turning the dataset into a csv
    data = list(reader)
print(data)
headers = data.pop(0)
print(headers)

# Plot Homicides by Firearm per 100k vs Firearms per 100 people
hom_per = []
firearm_per = []
countries_to_plot = ["United States", "France", "Canada", "Germany", "Japan", "South Korea", "England and Wales", "Ireland", "Sweden", "Norway", "Denmark", "Spain", "Australia", "Russia", "China"]
country_names = []
for i in range(len(data)):
    if data [i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            hom_per.append(homicide)
            firearm_per.append(firearm)
            country_names.append(data[i][0])
        except:
            print(data[i][0], "has no data")

plt.figure("Gun Stats", figsize=(9, 7))
plt.scatter(firearm_per, hom_per, s=25)
plt.title("World Homicide Rate vs. Firearm Ownership")
plt.xlabel("Number of Firearms per Person")
plt.ylabel("Number of Homicides per 100,000 People")
m, b = np.polyfit(firearm_per, hom_per, 1) # input the degree of the line of best fit, here it is one
x = [0, 100]
y = [m * point + b for point in x]
plt.plot(x, y)
for i in range(len(country_names)):
    plt.annotate(country_names[i], xy = (firearm_per[i], hom_per[i])) # text, xy = (x, y)
plt.show()




