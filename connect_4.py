import turtle, random 

screen = turtle.Screen()
screen.delay(0)

chip = turtle.Turtle()
chip.shape("circle")
chip.color("green")
chip.penup()
chip.speed(0)

CHIP_DIST = 30 # the distance each chip will be apart

connect = []

for i in range(7) :
    connect.append([])
    x = connect[i]
    for j in range(7) : 
        x.append(0)
        chip.goto(-90 + i * CHIP_DIST, -100 + j * CHIP_DIST)
        chip.stamp()
               
chip.color("blue")
chip.goto(-90 + 3 * CHIP_DIST, -100 + 7 * CHIP_DIST)

turn = 1
running = True

def r():
    if running :
        x = chip.xcor()
        if x < (-90 + CHIP_DIST * 6) : 
            chip.setx(x + CHIP_DIST)
        else :
            chip.setx(-90)
                        
def l():
    if running :
        x = chip.xcor()
        if x > -90 : 
            chip.setx(x - CHIP_DIST)
        else : 
            chip.setx(-90 + CHIP_DIST * 6)
            
def d():
    global turn, running
    if running :
        x = int(chip.xcor() / CHIP_DIST) + 3
        col = connect[x]
        for y in range(len(col)) :
            if(col[y] == 0) :
                chip.sety( -100 + y*CHIP_DIST)
                chip.stamp()
                chip.speed(0)
                chip.goto(-90 + 3 * CHIP_DIST, -100 + 7 * CHIP_DIST)
                connect[x][y] = turn
                if haswinner(x,y) :
                    running = False
                    style= ('Courier', 15, 'bold')
                    turtle.write("Player " + str(turn) + " is the winner!", font=style, align='center')
                else :
                    if turn == 1 : 
                        turn = 2
                        chip.color("red")
                    else : 
                        turn = 1
                        chip.color("blue")
                break
                
def checkrow(x,y) :
    count = 1
    for i in range(1,4) :
        if x + i < 7 and connect[x + i][y] == turn :
            count += 1
        else :
            break
    for i in range(1,4) :
        if x - i > -1 and connect[x - i][y] == turn :
            count += 1
        else :
            break
    if count >= 4 : 
        return True
    return False

def checkcolumn(x,y) :
    count = 1  
    for i in range(1,4) :
        if y + i < 7 and connect[x][y + i] == turn :
            count += 1
        else :
            break
    for i in range(1,4) :
        if y - i > -1 and connect[x][y - i] == turn :
            count += 1
        else :
            break
    if count >= 4 : 
        return True 
    return False

def checkdiag1(x,y) :
    count = 1  
    for i in range(1,4) :
        if y + i < 7 and x + i < 7 and connect[x + i][y + i] == turn :
            count += 1
        else :
            break
    for i in range(1,4) :
        if y - i > -1 and x - i > -1 and connect[x - i][y - i] == turn :
            count += 1
        else :
            break
    if count >= 4 : 
        return True 
    return False

def checkdiag2(x,y) :
    count = 1  
    for i in range(1,4) :
        if y + i < 7 and x - i > -1 and connect[x - i][y + i] == turn :
            count += 1
        else :
            break
    for i in range(1,4) :
        if y - i > -1 and x + i < 7 and connect[x + i][y - i] == turn :
            count += 1
        else :
            break
    if count >= 4 : 
        return True 
    return False

def haswinner(x,y) :        
    return checkrow(x,y) or checkcolumn(x,y) or checkdiag1(x,y) or checkdiag2(x,y)


                        
screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(d, "Down")
screen.listen()


