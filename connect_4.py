import turtle

screen = turtle.Screen()
screen.delay(0)

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.goto(1000, -1000)

chip = sprite.clone()
chip.shape("circle")
chip.color("green")

connect = []
CHIP_DIST = 30  # The distance between chips
ORIGIN_X = -90
ORIGIN_Y = -100
RIGHTMOST_COL = ORIGIN_X + CHIP_DIST * 6

for i in range(7):
    connect.append([])  # Create a column
    y = connect[i]  # Get the column you just created
    for j in range(7):  # Add to the column while drawing it
        chip.goto(ORIGIN_X + i * CHIP_DIST, ORIGIN_Y + j * CHIP_DIST)
        chip.stamp()
        y.append(0)

chip.color("blue")
chip.goto(ORIGIN_X + 3 * CHIP_DIST, ORIGIN_Y + 7 * CHIP_DIST)

running = True

def r():
    if running:
        x = chip.xcor()
        if x < RIGHTMOST_COL:
            chip.setx(x + CHIP_DIST)
        else:
            chip.setx(ORIGIN_X)

screen.onkey(r, "Right")
screen.listen()

def l():
    if running:
        x = chip.xcor()
        if x > ORIGIN_X:
            chip.setx(x - CHIP_DIST)
        else:
            chip.setx(RIGHTMOST_COL)

screen.onkey(l, "Left")

turn = 1

def d():
    global turn, running
    if running:
        # Get the column number where the chip dropped
        x = int((chip.xcor() - ORIGIN_X) / CHIP_DIST)
        col = connect[x]

        for y in range(len(col)):  # Indented correctly
            if col[y] == 0:
                chip.sety(ORIGIN_Y + y * CHIP_DIST)
                chip.stamp()
                chip.goto(ORIGIN_X + 3 * CHIP_DIST, ORIGIN_Y + 7 * CHIP_DIST)
                connect[x][y] = turn

                if haswinner(x, y):  # Check for winner after placing chip
                    running = False
                    style = ('Courier', 15, 'bold')
                    turtle.write("Player " + str(turn) + " is the winner!", font=style, align='center')
                else:
                    if turn == 1:
                        turn = 2
                        chip.color("red")
                    else:
                        turn = 1
                        chip.color("blue")
                break  # Stop after placing the chip

screen.onkey(d, "Down")

def haswinner(x, y):
    return checkrow(x, y) or checkcolumn(x, y)

def checkrow(x, y):
    count = 1
    for i in range(1, 4):
        if x + i < 7 and connect[x + i][y] == turn:
            count += 1
        else:
            break
    for i in range(1, 4):
        if x - i > -1 and connect[x - i][y] == turn:
            count += 1
        else:
            break
    return count >= 4

def checkcolumn(x, y):
    count = 1
    for i in range(1, 4):
        if y + i < 7 and connect[x][y + i] == turn:
            count += 1
        else:
            break
    for i in range(1, 4):
        if y - i > -1 and connect[x][y - i] == turn:
            count += 1
        else:
            break
    return count >= 4

screen.mainloop()  # Keeps the window open
