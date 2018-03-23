import turtle
import random
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_screen = turtle.Screen()
my_screen.bgcolor("white")
my_turtle.speed(0)

'''
# Draw A Shape Using the Goto Function
my_turtle.begin_fill() # place this before the code for the shape you want to fill in
my_turtle.fillco lor("yellow") # sets the fill color for the shape
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill() # this ends the fill for the shape in between the two fill functions

# Pick Up the Turtle
my_turtle.up() # like picking up your pencil, moves it to the location without drawing
my_turtle.goto(200, 200)
my_turtle.down() # places the turtle back down onto the "paper"
my_turtle.begin_fill()
my_turtle.fillcolor("pink")
my_turtle.goto(300, 300)
my_turtle.goto(300, 200)
my_turtle.goto(200, 200)
my_turtle.end_fill()

# Draw Using Headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(1) # changes the thickness of the lines (in pixels)
my_turtle.begin_fill()
my_turtle.fillcolor("pink")
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.setheading(360)
my_turtle.end_fill()

my_turtle.begin_fill()
my_turtle.fillcolor("pink")
for i in range(3):
    my_turtle.right(120)
    my_turtle.forward(200)
my_turtle.end_fill()

my_turtle.begin_fill()
my_turtle.fillcolor("yellow")
for i in range(6):
    my_turtle.right(60)
    my_turtle.forward(50)
my_turtle.end_fill()

# Rectangle Recursive Patterns
# my_screen.clear()
my_turtle.home()
def recursive_square(side_length, depth):
    x_pos = 0
    y_pos = 0
    if depth > 0:
        my_turtle.up()
        x_pos += 2
        y_pos -= 1
        my_turtle.goto((side_length / 2) + x_pos, (side_length / 2) + y_pos)
        my_turtle.begin_fill()
        my_turtle.fillcolor("pink")
        my_turtle.down()
        for i in range(4):
            my_turtle.right(90)
            my_turtle.forward(side_length)
        my_turtle.end_fill()
        recursive_square(side_length / 1.4, depth - 1)
    else:
        pass
recursive_square(400, 5)
my_screen.clear()
'''

# Recursive Fractal - NCAA Brackets
def recursive_NCAA(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + (size / 2))
        my_turtle.goto(x + size, y - (size / 2))
        recursive_NCAA(x + size, y + (size / 2), (size / 2), depth - 1)
        recursive_NCAA(x + size, y - (size / 2), (size / 2), depth - 1)
recursive_NCAA(-350, 0, 150, 7)

my_screen.exitonclick() # ends the program by clicking on the window, should be the last line in the code
