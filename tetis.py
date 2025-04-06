
import turtle, random

screen = turtle.Screen()
screen.bgcolor("black")
screen.delay(0)

sprite = turtle.Turtle()
sprite.penup()
sprite.speed(0)
sprite.color('white')
sprite.ht()

#Shapes Informations
shapes = {}
blocks = {}
blocks['j'] = ("blue", [(0,0),(-20,-20), (-20,0), (20,0)])
blocks['o'] = ("red", [(0,0),(0,-20), (-20,-20), (-20,0)])
blocks['z'] = ("green", [(0,0),(0,-20), (-20,0), (-20,20)])
blocks['l'] = ("yellow", [(0,0),(20,0), (-20,0), (-20,20)])
blocks['i'] = ("brown", [(0,0),(-20,0), (20,0),(40,0)])
blocks['s'] = ("violet", [(0,0),(0,20), (-20,0), (-20,-20)])
blocks['t'] = ("purple", [(0,0),(20,0), (0,-20), (0,20)])

shapes['p'] = ((-10,-10), (-10,10), (10,10), (10,-10))
shapes['j'] = ((-30,-30), (-30,10), (30,10), (30,-10), (-10,-10),(-10,-30))
shapes['o'] = ((-30,-30), (-30,10), (10,10), (10,-30))
shapes['z'] = ((-30,-10), (-30,30), (-10,30), (-10,10), (10,10),(10,-30),(-10,-30),(-10,-10))
shapes['l'] = ((-30,-10), (-30,30), (-10,30), (-10,10), (30,10),(30,-10))
shapes['i'] = ((-30,-10), (-30,10), (50,10),(50,-10))
shapes['s'] = ((-30,-30), (-30,10), (-10,10), (-10,30), (10,30),(10,-10),(-10,-10),(-10,-30))
shapes['t'] = ((-10,-30), (-10,30), (10,30), (10,10), (30,10),(30,-10),(10,-10),(10,-30))

for i,j in shapes.items():
    screen.register_shape(i,j)

sprite.shape('p')

#Game Set Up
block = sprite.clone()
block.st()
letter = ""
shape = ""

Left = -100
Right = 80
Bottom = -160
Top = 140
size = 20

pixels = {}

for i in range(Bottom,Top+size,size):
    pixels[i] = {}
    for j in range(Left,Right+size,size):
        pixels[i][j] = sprite.clone()
        pixels[i][j].goto(j,i)
        pixels[i][j].stamp()

#Game Loop
def reset():
    global letter, shape
    letter = "jozlist"[random.randint(0,6)]
    shape_info = blocks[letter]
    block.seth(0)
    block.goto(0,Top)
    block.shape(letter)
    block.color(shape_info[0])
    shape = shape_info[1][:]
    drop()

def drop():
    if(check_bound(0,-size,shape)):
        block.goto(block.xcor(),block.ycor()-size)
        screen.ontimer(drop, 800)
    else:
        if(block.ycor() != Top):
            add_to_bound()
            check_row()
            reset()

#Bounding Area
bound = {}
def check_bound(dx,dy,offsets):
    x = block.xcor()
    y = block.ycor()
    for i in offsets:
        ty = y+i[0]+dy
        tx = x+i[1]+dx
        if(ty < Bottom or tx < Left or tx > Right or (ty in bound.keys() and tx in bound[ty])):
            return False

    return True

def add_to_bound():
    x = block.xcor()
    y = block.ycor()
    for i in shape:
        ty = y+i[0]
        tx = x+i[1]
        if(ty not in bound.keys()):
            bound[ty] = set()

        bound[ty].add(tx)
        pixel = pixels[ty][tx]
        pixel.color(block.fillcolor())
        pixel.st()

#Keyboard Controls
def move_by(dx,dy):
    if(check_bound(dx,dy,shape)):
        block.goto(block.xcor()+dx,block.ycor()+dy)

def left():
    move_by(-size,0)

def right():
    move_by(size,0)

def down():
    move_by(0,-size)

def rotate_left():
    global shape
    t = []
    for i in shape:
        t.append((i[1],-i[0]))

    if(check_bound(0,0,t)):
        shape = t
        block.left(90)

def rotate_right():
    global shape
    t = []
    for i in shape:
        t.append((-i[1],i[0]))

    if(check_bound(0,0,t)):
        shape = t
        block.right(90)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(down, "Down")
screen.onkey(rotate_left, "A")
screen.onkey(rotate_right, "D")
screen.listen()

#Collapsing Rows
def check_row():
    full = (Right-Left+size)/size
    up=0
    t = sorted(bound.keys())
    for i in t:
        while(i+up in bound.keys() and len(bound[i+up]) == full):
            up+=size

        if(up>0):
            if(i+up in bound.keys()):
                bound[i] = set(bound[i+up])
                for k in pixels[i].keys():
                    if(pixels[i+up][k].isvisible()):
                        pixels[i][k].color(pixels[i+up][k].fillcolor())
                        pixels[i][k].st()
                    else:
                        pixels[i][k].ht()
            else:
                del bound[i]
                for v in pixels[i].values():
                    v.ht()

reset()
