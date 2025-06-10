#=====================================Day18=============================================
import random
from random import randint
import turtle as t
# def redirect_left(angle,move):
#     timmy.left(angle)
#     timmy.forward(move)
#
# def redirect_right(angle,move):
#     timmy.right(angle)
#     timmy.forward(move)
#
timmy = t.Turtle()
screen = t.Screen()
timmy.shape('turtle')
timmy.color('green')
timmy.pencolor('blue')


# redirect_left(90,100)
# redirect_left(90,100)
# redirect_left(90,100)
# redirect_left(90,100)

#
# for _ in range(50):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for n in range (3,11):
#     for i in range(0,n):
#         timmy.right(360/n)
#         timmy.forward(100)
# timmy.pensize(15)
timmy.speed("fastest")
# direction=[0,90,180,270]
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)#---------------------A tuple is a collection of elements that are ordered
#     -------------------------------------and can contain different types of data.__________(inside curly braces)
#     -------------------------------------Tuples are similar to lists, but they are immutable,
#     -------------------------------------meaning they cannot be changed after they are created.
#
# for i in range(100):
#     timmy.pencolor(random_color())
#     timmy.setheading(random.choice(direction))
#     timmy.forward(randint(25,150))

# def spiral(gap):
#     for i in range(int(360/gap)):
#         timmy.pencolor(random_color())
#         timmy.circle(100)
#         current_heading = timmy.heading()
#         timmy.setheading(current_heading+gap)
# spiral(2)
timmy.penup()
timmy.hideturtle()
timmy.left(215)
timmy.forward(240)
timmy.setheading(0)
for dots in range(1,101):
    timmy.dot(20,random_color())
    timmy.forward(50)
    if dots % 10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
screen.exitonclick()