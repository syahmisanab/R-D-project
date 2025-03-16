import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightgreen")

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.shape("square")
sprite.goto(-1000, 1000)

snake = []
dir = "Right"
food = None


def u():
    global dir
    if dir != "Down":
        dir = "Up"


def d():
    global dir
    if dir != "Up":
        dir = "Down"


def l():
    global dir
    if dir != "Right":
        dir = "Left"


def r():
    global dir
    if dir != "Left":
        dir = "Right"


def createBody(x, y):
    body = sprite.clone()
    body.goto(x, y)
    snake.append(body)


def move():
    last = snake[-1]
    first = snake[0]
    x = first.xcor()
    y = first.ycor()
    size = 22

    if dir == "Right":
        last.goto(x + size, y)
    elif dir == "Left":
        last.goto(x - size, y)
    elif dir == "Up":
        last.goto(x, y + size)
    else:
        last.goto(x, y - size)

    snake.insert(0, last)
    snake.pop()


def createFood():
    global food
    food = sprite.clone()
    food.color("red")
    randX = random.randint(-8, 8) * 22
    randY = random.randint(-8, 8) * 22
    food.goto(randX, randY)


running = False


def update():
    if running:
        move()
        first = snake[0]
        x = first.xcor()
        y = first.ycor()
        global food

        if x == food.xcor() and y == food.ycor():
            createBody(first.xcor(), first.ycor())
            food.hideturtle()
            createFood()

        screen.ontimer(update, 350)


def startGame():
    global running
    running = True
    createBody(0, 0)
    createFood()
    update()


screen.onkey(u, "Up")
screen.onkey(d, "Down")
screen.onkey(l, "Left")
screen.onkey(r, "Right")
screen.listen()

startGame()
