import turtle
import math

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x > -280:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < 280:
            self.goto(new_x, self.ycor())

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(x, y)

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=0.1, stretch_len=0.5)
        self.setheading(90)
        self.penup()
        self.hideturtle()
        self.speed = 15
        self.state = "ready"

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.goto(x, y + 10)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            self.goto(self.xcor(), self.ycor() + self.speed)
            if self.ycor() > 280:
                self.hideturtle()
                self.state = "ready"

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
bullet = Bullet()

enemies = []
for i in range(15):
    x = -200 + (i % 5) * 60
    y = 200 - (i // 5) * 40
    enemies.append(Enemy(x, y))

enemy_speed = 1.5

screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkey(lambda: bullet.fire(player.xcor(), player.ycor()), "space")

game_is_on = True
while game_is_on:
    screen.update()
    bullet.move()

    move_down = False
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy_speed)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            move_down = True

    if move_down:
        enemy_speed *= -1
        for enemy in enemies:
            enemy.sety(enemy.ycor() - 20)

    for enemy in enemies:
        if bullet.state == "fire" and math.dist((bullet.xcor(), bullet.ycor()), (enemy.xcor(), enemy.ycor())) < 20:
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -400)
            enemy.goto(1000, 1000)
            enemies.remove(enemy)
            break

        if math.dist((player.xcor(), player.ycor()), (enemy.xcor(), enemy.ycor())) < 20 or enemy.ycor() < -250:
            game_is_on = False
            pen = turtle.Turtle()
            pen.color("white")
            pen.hideturtle()
            pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            break

    if not enemies:
        game_is_on = False
        pen = turtle.Turtle()
        pen.color("white")
        pen.hideturtle()
        pen.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))

screen.exitonclick()