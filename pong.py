import turtle

sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# keep track of score
left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player: 0     Right Player: 0",
             align="center", font=("Courier", 24, "normal"))

def paddle_left_up():
    y = left_pad.ycor()
    y = y + 20
    left_pad.sety(y)
    if left_pad.ycor() >= 240:
        left_pad.sety(240)

def paddle_left_down():
    y = left_pad.ycor()
    y = y - 20
    left_pad.sety(y)
    if left_pad.ycor() <=-240:
        left_pad.sety(-240)

def paddle_right_up():
    y = right_pad.ycor()
    y = y + 20
    right_pad.sety(y)
    if right_pad.ycor() >= 240:
        right_pad.sety(240)

def paddle_right_down():
    y = right_pad.ycor()
    y = y - 20
    right_pad.sety(y)
    if right_pad.ycor() <= -240:
        right_pad.sety(-240)

# key bindings
# onkeyrelease instead of onkeypressed, so people dont keep their fingers on the keyboard 
sc.listen()
sc.onkeyrelease(paddle_left_up, "w")
sc.onkeyrelease(paddle_left_down, "s")
sc.onkeyrelease(paddle_right_up, "Up")
sc.onkeyrelease(paddle_right_down, "Down")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy = hit_ball.dy * -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy = hit_ball.dy * -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy = hit_ball.dy * -1
        left_player = left_player + 1
        sketch.clear()
        sketch.write("Left Player: {}     Right Player: {}".format(
            left_player, right_player), align="Center",
            font=("Courier", 24, "normal"))
        
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy = hit_ball.dy * -1
        right_player = right_player + 1
        sketch.clear()
        sketch.write("Left Player: {}     Right Player: {}".format(
            left_player, right_player), align="Center",
            font=("Courier", 24, "normal"))
        
    # paddle collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() -50):
        hit_ball.setx(360)
        hit_ball.dx = hit_ball.dx * -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() -50):
        hit_ball.setx(-360)
        hit_ball.dx = hit_ball.dx * -1