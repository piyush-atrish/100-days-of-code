from turtle import Turtle,Screen
import time

class Board(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(x,y)

    def up(self):
        if self.ycor() < 250:
            self.setheading(90)
            self.forward(20)
    def down(self):
        if self.ycor() > -250:
            self.setheading(270)
            self.forward(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.09

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()


class Scorecard(Turtle):
    def __init__(self,x,y,n):
        super().__init__()
        self.score=0
        self.number= f'Player {n}'
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x, y)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f'{self.number}\nSCORE: {self.score}',False,'center',('arial',20,"bold"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER\n{self.number}Win', False, 'center', ('arial', 25, "bold"))

screen = Screen()
screen.title('bong')
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
player1=Board(-380,0)
player2=Board(370,0)
screen.onkey(player1.up,"w")
screen.onkey(player1.down,"s")
screen.onkey(player2.up,"Up")
screen.onkey(player2.down,"Down")
ball=Ball()
score_1 = Scorecard(-200, 230, 1)  # Position on the left, near the top
score_2 = Scorecard(200, 230, 2)   # Position on the right, near the top


is_on=True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(player2) < 50 and ball.xcor() > 320) or \
       (ball.distance(player1) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_1.update()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_2.update()

screen.exitonclick()
