import csv
import matplotlib.pyplot as plt

with open("data/library_data") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

names = [x[0] for x in data]  # grabbing list of library names (alphabetical)
names = names[1:]  # chop off header
print(names)

ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd]
print(ytd)

library_number = [x for x in range(len(names))]
print(library_number)

# We want to plot computer users YTD vs library.

plt.figure(1, figsize=(12, 8), tight_layout=True, facecolor="lightblue")
plt.bar(library_number, ytd, color='red')
plt.title("Chicago Library Branch Computer Usage - 2017")
plt.ylabel("Computer Users")

plt.xticks(library_number, names, rotation=90, fontsize=8)  #  plotted data, text to plot

# Make a line graph of comp users at three libraries by month
print(data)
month_names = data.pop(0)[1:-1]
print(month_names)
month_numbers = [x for x in range(12)]
print(month_numbers)
library_names = [x[0] for x in data]
print(library_names)

bwp_data = data[library_names.index("Bucktown-Wicker Park")]
bwp_data.pop(0)
bwp_data.pop() # pops the last value on the list
bwp_data = [int(x) for x in bwp_data]
print(bwp_data)

bwp_data = data[library_names.index("Bucktown-Wicker Park")]
bwp_data.pop(0)
bwp_data.pop() # pops the last value on the list
bwp_data = [int(x) for x in bwp_data]
print(bwp_data)

lp_data = data[library_names.index("Lincoln Park")][1:-1]
lp_data = [int(x) for x in lp_data]
print(lp_data)


print(month_numbers)
print(bwp_data)

plt.figure(2)
plt.plot(month_numbers, lp_data, label="Lincoln Park")
plt.legend(bbox_to_anchor=(0.9, 0.9), loc="upper right")
plt.xticks(month_numbers, month_names, rotation=45)


plt.show()