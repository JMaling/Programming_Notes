#  SEARCHING (Chapter 15 from programarcadegames.com)
import random
import re

file = open("Data/Villains.txt", "r")  # open file to read (creates object named file) and pulls it from file "Data"
print(file)
for line in file:
    print(line.strip())  # .strip() method removes spaces, tabs, and returns from the beginning and the end
file = open("Data/Villains.txt", "r")
for line in file:
    print("Hello", line.strip()) # python's "cursor" is at the bottom of the file already, so it can read through again
file.close()

# You can also open a file to write
# file = open("Data/Villains.txt", "w")  # open file to write (creates object named file) and pulls it from file "Data"
# file.write("JACK")  # overwrites everything else on the file with your new text
# file.close()

# You can also open a file to append
# file = open("Data/Villains.txt", "a")
# file.write("Lee the Merciless\n")
# file.close()

# Read the file into an array (list)
file = open("Data/Villains.txt", "r")
'''
villains = []
for line in file:
    villains.append(line.strip())
'''
villains  = [x.strip() for x in  file]
print(villains)

# Linear Search (not very efficient)
key = villains[27] # thing that we are searching for
i = 0 # index for the loop
while i < len(villains) - 1 and key != villains[i]:
    i += 1
if i < len(villains):
    print("Found the", key, "at position", i)

# Binary Search (Far more efficient with processing power than a linear search)
key = villains[random.randrange(101)]
lower_bound = 0
upper_bound = len(villains) - 1 # The final position in the list is actually 99, because the counting starts at 0
found = False
count = 0
while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
        count += 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
        count += 1
    else:
        count += 1
        found = True
if found:
    print(key, "Was Found At Position", middle_pos, "In", count, "Tries")
else:
    print(key, "Was Not Found In The List")

# Extra Stuff
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
file = open(Data/villains.txt)
all_words = []
for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)
print(all_words)
for word in all_words:
    print(len(word))

