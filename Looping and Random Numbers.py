# LOOPS AND RANDOM NUMBERS

# FOR LOOPS
for i in range(10):
    print(i)
for i in range(3, 9):
    print(i)
for i in range(-5, 1):
    print(i)
for i in range(10, 50, 5):
    print(i)
# RANDOM NUMBERS
import random
print(random.randrange(10))
print(random.randrange(5, 16))
print(random.randrange(-5, 5))
print(random.randrange(50, 100, 5))  # prints a random number from 50 - 100, that is a multiple of 5
print(random.randrange(10, -11, -2))  # the "jump distance" must match the direction of the travel ( + + ), ( - - )
# Random Floats:
print(random.random())  # prints a random float from 0 to 1
print(random.random() * 10 + 5)  # prints a random float from 5 - 15

# BREAK, CONTINUE, FOR ELSE
# BREAK
# Immediately exits (or breaks out of) the current loop
for i in range(100):
    roll = random.randrange(1, 7)
    print("You rolled a ", roll, "on roll number", i)
    if roll == 6:
        break
# CONTINUE
# Skips the rest of the current iteration, so in this case,
# it will go back to the top, and not print any of the odd numbers
for i in range(10):
    roll = random.randrange(1, 7)
    if roll % 2:
        continue
    print(roll)
# FOR ELSE
# If you make it all the way through the for loop without breaking
# then you do the ELSE statement

for i in range(10):
    n = random.randrange(10)
    print(n)
    if n == 0:
        break
else:
    print("Didn't roll 0")