'''
Functions and Module Notes
By: Jack Maling
'''
from random import *  # random is a library or module, * is the wildcard
# import math  # imports go at the top of your program
from math import pi
import MyModule
#  When you use the keyword from, you are importing directly into your file
# no need to use random.randrange, just use randrange

# FUNCTIONS AND MODULES
print(randrange(900, 1000))

if __name__ == "__main__":  # this code only runs if this is the executed code/file
    print(randrange(100))
    print(random())
    e = 5
    print(e)
    print(pi)
    print("This is Period:", MyModule.period)
    MyModule.hello("Jack")
    MyModule.product_sum(10, 20)
    product, sum = MyModule.product_sum(100, .89)
    print(product, sum)

    print(3, 4, sep = ", ", end = "")
    print(5, 6)
    MyModule.hello(name = "Francis")
    MyModule.hello()

