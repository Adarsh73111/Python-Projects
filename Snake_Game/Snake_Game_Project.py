# from turtle import Screen, Turtle
# import time
# import random
#
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
#
# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         new_segment = Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#
#     def extend(self):
#         self.add_segment(self.segments[-1].position())
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
#
# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=0.5, stretch_wid=0.5)
#         self.color("blue")
#         self.speed("fastest")
#         self.refresh()
#
#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)
#
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
#
#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
#
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
#
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()
#
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()
#
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#
# screen.exitonclick()

# from turtle import Screen, Turtle
# import time
# import random
#
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
#
# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         new_segment = Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#
#     def reset(self):
#         for seg in self.segments:
#             seg.goto(1000, 1000)
#         self.segments.clear()
#         self.create_snake()
#         self.head = self.segments[0]
#
#     def extend(self):
#         self.add_segment(self.segments[-1].position())
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
#
# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=0.5, stretch_wid=0.5)
#         self.color("blue")
#         self.speed("fastest")
#         self.refresh()
#
#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)
#
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.high_score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.clear()
#         self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
#
#     def reset(self):
#         if self.score > self.high_score:
#             self.high_score = self.score
#         self.score = 0
#         self.update_scoreboard()
#
#     def increase_score(self):
#         self.score += 1
#         self.update_scoreboard()
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake Game High Score")
# screen.tracer(0)
#
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
#
# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()
#
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         scoreboard.reset()
#         snake.reset()
#
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             scoreboard.reset()
#             snake.reset()
#
# screen.exitonclick()

# Advance Version

from turtle import Screen, Turtle
import time
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class BonusFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("gold")
        self.speed("fastest")
        self.goto(1000, 1000)

    def show(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def hide(self):
        self.goto(1000, 1000)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 20, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Arcade Snake")
screen.tracer(0)

snake = Snake()
food = Food()
bonus_food = BonusFood()
scoreboard = Scoreboard()

is_paused = False


def toggle_pause():
    global is_paused
    is_paused = not is_paused


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "space")

game_is_on = True
current_delay = 0.1
bonus_timer = 0

while game_is_on:
    screen.update()

    if not is_paused:
        time.sleep(current_delay)
        snake.move()

        # Standard Food Collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score(1)
            # Speed up the game slightly
            if current_delay > 0.05:
                current_delay *= 0.98

            # Chance to spawn bonus food
            if random.randint(1, 5) == 1:
                bonus_food.show()
                bonus_timer = 50

                # Bonus Food Logic
        if bonus_timer > 0:
            bonus_timer -= 1
            if snake.head.distance(bonus_food) < 20:
                bonus_food.hide()
                scoreboard.increase_score(3)
                snake.extend()
                bonus_timer = 0
        elif bonus_timer == 0:
            bonus_food.hide()

        # Wall Collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()
            current_delay = 0.1
            bonus_food.hide()

        # Tail Collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                current_delay = 0.1
                bonus_food.hide()

screen.exitonclick()

