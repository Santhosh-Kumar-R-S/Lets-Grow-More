import random
import turtle
import time

# Creating Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)  # Corrected 'hight' to 'height'
screen.tracer(0)
screen.bgcolor('#1d1d1d')

# Creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed(0)  # Added an argument to 'snake.speed()'
snake.shape('square')
snake.color('green')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color("White")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 260)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))


# Define how to move
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard Binding
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main Loop
while True:
    screen.update()

    # Snake and Fruit Collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # Creating new food
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Adding ball to the Snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    
    move()  # Corrected from 'snake_move()' to 'move()'

    # Snake & Border Collision
    if snake.xcor() > 290 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:  # Fixed conditions
        time.sleep(1)  # Added sleep time
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("     Game Over\n Your Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

    # Snake Collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)  # Added sleep time
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("     Game Over\n Your Score is {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)

turtle.Terminator()
