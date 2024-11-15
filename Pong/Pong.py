import turtle
from pygame import mixer

#  sound mixer
mixer.init()

# sound file
bounce_sound = mixer.Sound('bounce.wav')

wind = turtle.Screen()
wind.title("Pong by your Chaz")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Functions
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

 

# Up and down key movements
wind.listen()
wind.onkeypress(paddle_a_up, "w")
wind.onkeypress(paddle_a_down, "s")
wind.onkeypress(paddle_b_up, "Up")
wind.onkeypress(paddle_b_down, "Down")


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",24, "normal"))


# Score
score_a = 0
score_b = 0

while True:
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound.play()

        
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound.play()


    # Left and Right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        

    #Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        bounce_sound.play()



    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        bounce_sound.play()
    