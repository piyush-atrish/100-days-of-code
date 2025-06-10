#=======================================Day 20============================================

from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

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


is_on = True

snake = Snake()


while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.down,"Down")
    screen.listen()



screen.exitonclick()