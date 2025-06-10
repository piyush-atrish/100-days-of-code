#======================================day21=============================================
# Inheritance -------------->
# allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# example:
# class Animal:
#     def __init__(self):
#         self.eyes=2
#
#     def breathe(self):
#         print('inhale exhale')
#
# class Fish(Animal):        #------the one in bracket is the parent class
#     def __init__(self):
#         super().__init__()   #-----allows to call method and argument of super classes
#         self.eyes=3          #------can change
#
#     def breathe(self):
#         super().breathe()     #-------can add more in methods
#         print('can do this under water')
#
#     def swim (self):
#         print("moving under water")
#
# fishy=Fish()
# fishy.breathe()
# print(fishy.eyes)
# fishy.swim()


from turtle import Turtle, Screen
import random
import time

class Snake:

    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
            x1=0
            for _ in range(4):
                block=Turtle('square')
                block.color('white')
                block.penup()
                block.goto(x=x1,y=0)
                x1-=20
                self.snake.append(block)

    def extend(self):
        block = Turtle('square')
        block.color('white')
        block.penup()
        block.goto(self.snake[-1].position())
        self.snake.append(block)

    def move(self):
            for i in range(len(self.snake) - 1, 0, -1):
                x2 = self.snake[i - 1].xcor()
                y2 = self.snake[i - 1].ycor()
                self.snake[i].goto(x2, y2)
            self.head.forward(20)

    def up(self):
        if self.head.heading() != 270 :
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90 :
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0 :
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180 :
             self.head.setheading(0)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
        

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f'SCORE: {self.score}',False,'center',('arial',20,"bold"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, 'center', ('arial', 25, "bold"))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_on = True
snake = Snake()
food = Food()
scorecard=Scorecard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.listen()

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scorecard.update()
        snake.extend()
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 290 or snake.head.ycor()< -280:
        scorecard.game_over()
        is_on = False
    for body in snake.snake[1:]: #----------------> this is called slicing
        if snake.head.distance(body) < 15:
            scorecard.game_over()
            is_on = False


screen.exitonclick()

# slicing is a method to get a specific part of a list/tuple/string in a modified way
# for example
#     list[1:5] of [1,2,3,4,5] will iterate through [2,3,4]
#     list[1:] gives [2,3,4,5]
#     list [:5] gives [1,2,3,4]
#     list [1:2:2] gives [2,4]
#     list[::-1] gives [5,4,3,2,1]
