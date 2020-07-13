## Simple Pong in Python3 
import turtle
import os

wn = turtle.Screen()
wn.title("Pong by me")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

## Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

## Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop 
while True:
    wn.update()

   
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
    
    if ball.xcor() > 360:
        ball.goto(0, 0)
        ball.dx *= -1
        if score_a < 6:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
            os.system("aplay point_a.wav&")

        elif score_a >= 6:
            pen.clear()
            turtle.clearscreen()
            os.system("aplay win_a.wav&")
            wn.bgcolor("black")
            pen.goto(0,0)
            pen.write("PLAYER A WINS", align="center", font=("Courier", 50, "normal"))


    if ball.xcor() < -360:
        ball.goto(0, 0)
        ball.dx *= -1
        if score_b < 6:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
            os.system("aplay point_b.wav&")
        elif score_b >= 6:
            pen.clear()
            turtle.clearscreen()
            os.system("aplay win_b.wav&")
            wn.bgcolor("black")
            pen.goto(0,0)
            pen.write("PLAYER B WINS", align="center", font=("Courier", 50, "normal"))
   
        

    
    # Paddle and ball collisions

 ## Paddle A
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("aplay bounce.wav&")

    ## Paddle B
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("aplay bounce.wav&")

   