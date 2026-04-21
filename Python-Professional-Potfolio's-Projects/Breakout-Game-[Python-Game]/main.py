import turtle
import time

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        new_x = self.xcor() - 40
        if new_x > -340:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 40
        if new_x < 340:
            self.goto(new_x, self.ycor())

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.02

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

class Brick(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1.2, stretch_len=3.5)
        self.penup()
        self.goto(x, y)

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()

bricks = []
colors = ["#FF5733", "#FFC300", "#DAF7A6", "#33FFBD", "#3380FF"]
y_start = 250

for i in range(5):
    for x in range(-350, 360, 75):
        brick = Brick(x, y_start)
        brick.color(colors[i])
        bricks.append(brick)
    y_start -= 35

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 60 and ball.ycor() < -230 and ball.y_move < 0:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 40:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.bounce_y()
            break

    if ball.ycor() < -290:
        game_is_on = False
        pen = turtle.Turtle()
        pen.color("white")
        pen.hideturtle()
        pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    if not bricks:
        game_is_on = False
        pen = turtle.Turtle()
        pen.color("white")
        pen.hideturtle()
        pen.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))

screen.exitonclick()

# import turtle
# import time
#
# class Paddle(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=1, stretch_len=6)
#         self.penup()
#         self.goto(0, -256)
#
#     def move_left(self):
#         new_x = self.xcor() - 40
#         if new_x > -340:
#             self.goto(new_x, self.ycor())
#
#
#     def move_right(self):
#         new_x = self.xcor() + 40
#         if new_x < -340:
#             self.goto(new_x, self.ycor())
#
#     class Ball(turtle.Turtle):
#         def __init__(self):
#             super().__init__()
#             self.shape("circle")
#             self.color("white")
#             self.penup()
#             self.x_move = 5
#             self.y_move = 5
#             self.move_speed = 0.02
#
#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x, new_y)
#
#     def bounce_y(self):
#         self.y_move *= -1
#
#     def bounce_x(self):
#         self.x_move *= -1
#
# class Brick(turtle.Turtle):
#     def __init__(self, x, y):
#         super().__init__()
#         self.shape("square")
#         self.color("blue")
#         self.shapesize(stretch_wid=1.2, stretch_len=3.5)
#         self.penup()
#         self.goto(x, y)
#
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Breakout")
# screen.tracer(0)
#
# paddle = Paddle()
# ball = Ball()
#
# bricks = []
# colors = ["#FF5733", "#FFC300", "#DAF7A6", "#33FFBD", "#3380FF"]
# y_start = 250
#
# for i in range(5):
#     for x in range(-350, 360, 75):
#         brick = Brick(x,y_start)
#         brick.color(colors[i])
#         bricks.append(brick)
#     y_start -= 35
#
# screen.listen()
# screen.onkeypress(paddle.move_left, "Left")
# screen.onkeypress(paddle.move_right, "Right")
#
# game_is_on = True
# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()
#
#     if ball.xcor() > 380 or ball.xcor() < -380:
#         ball.bounce_x()
#
#     if ball.ycor() > 280:
#         ball.bounce_y()
#
#     if ball.distance(paddle) < 60 and ball.ycor() < -230 and ball.y_move < 0:
#         ball.bounce_y()
#
#     for brick in bricks:
#         if ball.distance(brick) < 40:
#             brick.goto(1000, 1000)
#             bricks.remove(brick)
#             ball.bounce_y()
#             break
#
#     if ball.ycor() < -290:
#         game_is_on = False
#         pen = turtle.Turtle()
#         pen.color("white")
#         pen.hideturtle()
#         pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
#
#     if not bricks:
#         game_is_on = False
#         pen = turtle.Turtle()
#         pen.color("white")
#         pen.hideturtle()
#         pen.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))
#
#     screen.exitonclick()