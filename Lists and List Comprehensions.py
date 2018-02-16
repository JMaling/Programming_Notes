# LISTS AND LIST COMPREHENSIONS
import random

#  Basic List Stuff
print("FrAnCis PaRkEr".lower())
name = "Francis Parker"
for char in name:
    print(char.lower(), char)
my_list = ["Bev", "Abe", "Cam", "Dam", "Eve", "Flo", "Gus"]
my_numlist = [8, 3, 4, 5, 2, 1]
print(my_list[3])
my_list[3] = "Dammiem"
print(my_list[3])

#  Slicing
print(my_list[3:5]) #  prints index three and four (last number not included)
print(my_list[:4]) #  prints from the beginning of the list to the third object
print(my_list[4:]) #  prints from four to the end
print(my_list[:]) #  prints the whole list

#  Copying a List
my_list_copy = my_list #  just points to the orginal place in the memory
my_list_copy[-1] = "Gob" #  you can use negative indices
print(my_list_copy)
print(my_list)
my_list_copy = my_list[:] #  this copies the whole list into a new one
my_list_copy[-2] = "Feb"
print(my_list_copy)
print(my_list)

# METHODS FOR LISTS AND FUNCTIONS
#  Find the Index
print(my_list.index("Bev")) #  Finds only the first item in the list (would not locate a second "Deb")

# Finding out if an item exists in a list
print("Deb" in my_list)

# Find the min a max of a list
print(min(my_numlist))
print(max(my_numlist))
print(min(my_list)) #  Alphabetical (sort of) goes by the ordinal number (see the Ascii Chart)
print(ord("A"))
print(ord("a"))

# Find the Summation of a List
print(sum(my_numlist))

#  Find How Many times an item appears in a list
print(my_list.count("Gob"))

#  Add to a list
my_list.append("Gob")
print(my_list.count("Gob"))

#  Insert a value into a list
my_list.insert(3, "Don")

#  Sort a List
print(my_list)
my_list.sort()
print(my_list) #  Again, sorts according to the ordinal values

#  Reverse a list
my_list.reverse()
my_list[my_list.index("Abe")] = "Abe"
print(my_list)

# Clear a List
my_list_copy.clear()
print(my_list_copy)

# Pop - removes an item from the list AND returns it
print(my_list)
removed_name = my_list.pop() #  The default option removes the last item (pops it off)
print(my_list)
print(removed_name)
my_list.pop(my_list.index("Dammiem"))
print(my_list)
first_name = my_list.pop(0)
print(my_list)
print(first_name)

# Delete and Item from the List
del my_list[1]
print(my_list)
del my_list[1:]
print(my_list)

# ITERATING
#  For Each Loop - does not alter the original list
for item in my_numlist:
    item *= 2
    print(item)
print(my_numlist)

# Index Variable Loop - can actually alter the items in the list
for i in range(len(my_numlist)):
    my_numlist[i] *= 2
    print(my_numlist[i])
print(my_numlist)

# CREATE LISTS
# Make a list of numbers 1-100
my_numlist2 = []
for i in range(1, 101):
    my_numlist2.append(i)
print(my_numlist2)

# Go back through the list and square every number in the list
for i in range(len(my_numlist2)):
    my_numlist2[i] **= 2
print(my_numlist2)

# Make a two dimensional list that is 10 x 10 [[0, 0], [0, 1], [0, 2] ... [9, 9]]
my_list3 = []
for i in range(10):
    for j in range(10):
        my_list3.append([i, j])
print(my_list3)

# Print all of the individual pairs
for i in my_list3:
    print(i)

# add ten to each item y using iteration
for i in range(len(my_list3)):
    my_list3[i][1] += 10

# LIST COMPREHENSIONS
# Make a list of numbers from 0 to 99 and print it
my_list6 = []
for i in range(100):
    my_list6.append(i)
print(my_list6)
# now do it using list comprehensions:
my_list = [x for x in range(100)] #  the first x is the item going into the list, the second x is the iterator, and then the range is the range
print(my_list)

# Square every item in the previous list and print it
for i in range(len(my_list)):
    my_list[i] **= 2
print(my_list)
# now using list comprehensions:
my_list = [x ** 2 for x in range(100)]
my_list = [x for x in my_list]
print(my_list)

# Alter the list to only show the odd numbers and print it
my_list2 = []
for item in my_list:
    if item % 2 == 1:
        my_list2.append(item)
# now using list comprehensions:
my_list2 = [x for x in my_list if x % 2 == 1]
print(my_list2)
# Alter the list to only show numbers between 100 and 1000 and print it
my_list7 = []
for i in my_list2:
    if i >= 100 and i <= 1000:
        my_list7.append(i)

my_list7 = [x for x in my_list2 if x >= 100 and x <= 1000]
print(my_list7)

# Now do all four of these things at the same time
my_list5 = []
my_list5 = [x ** 2 for x in range(100) if (x ** 2) % 2 == 1 and (x ** 2) >= 100 and (x ** 2) <= 1000]
print(my_list5)

# LIST COMPREHENSIONS PRACTICE PROBLEMS - [returned item for iterator in range_or_list filter]
# roll a single die 100 times an put it in a list
die_list = []
die_list = [random.randrange(1, 7) for x in range(100)]
# roll two die pairs and 100 times and put them in a list
die_list = [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)]
# create a list of only the doubles from the rolls
double_list = [x for x in die_list if x[0] == x[1]]
print(double_list)
# can we create a list generator and filter on a single line
total_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]
print(total_list)  # basically establishes a list within the list that iterates through and assigns values to x, which the "outer" list can check and return






