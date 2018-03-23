# PLOTTING (With matplotlib)
import matplotlib.pyplot as plt  # makes it so that everytime we call it , we can just call it plt

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



plt.show()




