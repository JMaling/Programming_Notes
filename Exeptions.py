# EXEPTIONS

try:
    user_val = int(input("Enter a Number: "))
except:
    print("User Entered an Invalid Value")

# Error Types
try:
    int("A")
except ValueError: # improper values or types in a function
    print("Value Error")

# Divide by Zero Error
try:
    x = 7 / 0
except ZeroDivisionError:
    print("Cannot Divide by Zero")

# Input Output Error
try:
    my_file = open("my_file.txt")
except FileNotFoundError:
    print("File Cannot be Found")
except IOError:
    print("File Cannot be Found")
except: # general catchall
    print("Everything Went Wrong")

# Identifying Errors
try:
    y = 10 / 0
except Exception as e:
    print(e) # takes the exception object and prints it out, telling you what the error was

# A Better Way to Ask For Input From The User
# MPG Calculator
value_entered = False
while not value_entered:
    try:
        user_miles = int(input("Enter Miles: "))
        user_gallons = int(input("Enter Gallons: "))
        value_entered = True
    except:
        print("User Entered an Invalid Value")
try:
    print("MPG = ", user_miles / user_gallons, "Miles per Gallon")
except ZeroDivisionError:
    print("Cannot Divide By Zero")


