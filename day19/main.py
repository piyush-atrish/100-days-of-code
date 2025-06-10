#------------------------------------------day19----------------------------------------------

# def lowfunc(something)            -->higher order function
#   blah blah blah                     A higher-order function is a function that either takes one
#   return                             or more functions as arguments or returns a function or value as its result.

# def highfun(something)
#     blah blah blah
#     return somefunctionmaybe()
#
# highfun(lowfunc)--------------------> don't use parenthesis when using function as arguments



# from turtle import Turtle, Screen
#
# tim=Turtle()
# screen = Screen()
#
# def forward():
#     tim.forward(10)
# def backward():
#     tim.backward(10)
# def left():
#     tim.left(10)
# def right():
#     tim.right(10)
# def clear():
#     tim.clear()
#
# screen.onkey(key='w', fun=forward)
# screen.onkey(key='s', fun=backward)
# screen.onkey(key='a',fun=left)
# screen.onkey(key='d',fun=right)
# screen.onkey(key='c',fun=clear)
#
# screen.listen()
#
# screen.exitonclick()

from turtle import Turtle, Screen
import random

color=['red','blue','green','yellow','cyan','magenta']
screen = Screen()
screen.setup(width=500, height=400)
turtles=[]
y1=-150

for i in color:
    tim=Turtle(shape='turtle') #---------------------------> created multiple instances of the class turtle
    tim.color(i)
    tim.penup()
    tim.goto(-220,y1)
    y1+=60
    turtles.append(tim)

bet=screen.textinput(title='Make your bet',prompt='which turtle will win the race? enter a color: ')

if bet:
    race=True

while race:

    for tim in turtles:
        tim.forward(random.randint(1,10))
        if tim.xcor() > 220:
            winner=tim.pencolor()
            if winner==bet:
                print(f'you win!! {winner} is the winner')
            else:
                print(f'you lose!! {winner} is the winner')
            race=False


screen.exitonclick()

