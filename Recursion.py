# RECURSION (Function Calling Itself)

# Functions can call functions

def f():
    print("f")
    g()
def g():
    print("g")
    # f() - Will print a very specific error (nests forever)
f()

# Functions can call themselves
def hello(count):
    print("Hello", count)
    # hello(count + 1) #  Again, prints a very specific error (nests forever)
hello(1)

# Controlling Recursive Functions
def controlled(depth):
    print(depth)
    if depth > 0:
        controlled(depth - 1)
    else:
        pass
controlled(10) # Will run the function 100 times, but will only do so within the "legal" nesting amount

# Factorial
n = 10 # find the factorial
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

# Recursive Factorial
def factorial(num):
    if num > 1:
        return num * factorial(num -1)
    else:
        return num
print(factorial(10))
