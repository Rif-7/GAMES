import turtle

wn = turtle.Screen()
wn.title("Pong by Rif")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score Variables

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.color("white")
ball.penup()
ball.shape("square")
ball.goto(0, 0)
ball.speed(2)
ball.dx = .2
ball.dy = .2

# Score Board

j = True

if j:

    sb = turtle.Turtle()
    sb.color("white")
    sb.penup()
    sb.speed(0)
    sb.goto(0, 260)
    sb.hideturtle()
    sb.write("Player A:" + str(score_a) + "  Player B:" + str(score_b), align="center", font=("Courier", 24, "normal"))


# Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Functions

wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
i = True
while i:

    wn.update()

    # Making the ball move

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Fixing borders

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sb.clear()
        sb.write("Player A:" + str(score_a) + "  Player B:" + str(score_b), align="center",
                 font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sb.clear()
        sb.write("Player A:" + str(score_a) + "  Player B:" + str(score_b), align="center",
                 font=("Courier", 24, "normal"))

    # Ball and Paddle collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    if score_a == 3 or score_b == 3:

        i = False
        j = False


if score_a == 3:
    wn.update()
    sb.goto(0, 260)
    sb.write("Player A won.")
elif score_b == 3:
    sb.goto(0, 260)
    sb.write("Player B won.")

print("Somebody won, I'm too lazy to code that :)")



