# Math and Formatting

# Floats vs Ints
my_int = 1
my_float = my_int / 2
print(my_int / my_float)
print(my_float + 1.2)
print(1.2 / 2 + 1.2)
print("jack" + "maling")

# VARIABLES

# Naming (Allowed)
snake_case = "lowercase with underscores between words"
camelCase = "new words are capitalized"
# Naming (Not Allowed)
# tax% = num
# 8ball = 8
# ball8 = 8
# my variable = false

# Assignment Operator - Equal Sign
# One of the only way to change a variable
x = 5
# x + 1
print(x)
x = x + 1
print(x)

# MATH OPERATORS
# + - * /
# **        exponent
# //        similar to int (rounds down)
print(3.8 // 2)  # divides and chops off the decimal remainder
print(3.8 /2)  # divides and leaves the remainder
# %         modulo, gives the remainder after division
print(3.8 % 2)
print(3.8 / 2)

# COMPOUND ASSIGNMENT OPERATORS
# +=, -=, *=, /=
y = 2
y += 2 # y = y + 2
print(y)
y **= 3
print(y)

# ROUND FUNCTION
x = 1.987654323456
print(round(x, 2))  # rounds x to two digits
print(round(x, 0))  # rounds to 0 decimals
print(round(x, -1))  # rounds to the ones place

# FORMAT "{}".format()
# LANGUAGE FORMATTING
# for formatting TEXT
# Position:PlaceholderJustificationWidthDecorations
# Lets format some text:
first = "Jerry"
last = "Garcia"
invite_list = [["Abe", "Anderson"], ["Bev", "Beverly"], ["Chris", "Carter"]]
# print the first name:
print("{}".format(first))
# print first last
print("First: {} \tLast: {}".format(first, last))
# print last, first
print("{1}, {0}".format(first, last))
# print the invite list
for person in invite_list:
    print("{} {}, Would you like to come to my party?".format(person[0], person[1]))

# NUMBER FORMATTING
# you may specify d for digit/int, f for float, e for exponent to force a format
# here are some common uses
# round a float to a decimal place  {:.3f} rounds to 3
pi = 3.14159265358979
print("{:.4f}".format(pi))
# add a sign to number
# this works for both positive and negative numbers
print("{:-}".format(pi))
# add comma formatting a number ({:,})
my_number = 12341234567890
print("{:+,.4f}".format(my_number))

# Alignment:
# right align :>x where x is the width of the text
# print("{:>"+str(len(pi))+"}".format(pi))
print("{:>30}".format(pi))
# center align = :^x
print("{:^30}".format(pi))
# left align = :>x
print("{:<30}".format(pi))
# percent {:%} {:.2%}
print("{:>20.2%}".format(0.5678))
# exponent {:e} {:.2e}
print("{:.2e}".format(1234567890))
# leading zero (placeholder) {:05}
print("{:05}".format(23))

# dollars and cents?
# 142.3 to $142.3
x = 142.3
print("${:.2f}".format(x))
