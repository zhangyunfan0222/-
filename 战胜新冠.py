# 1. 安装freegames,  pip install freegames
# 2. 选择Cannon游戏作为模板
#        https://grantjenks.com/docs/freegames/#cannon
# 3. 添加新冠病毒图片
# 4. 发射疫苗，干掉病毒


from random import randrange
from turtle import *
from freegames import vector
import math


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
turtles = []
total_virus = 100
current_virus = 0
tr_medicine = Turtle()
tr_medicine_degree = 0.0
tr_girl = Turtle()
tr_boy = Turtle()

def add_shapes():
    addshape('res/virus.gif')

    for i in range(10):
        addshape(f'res/medicines/medicine_{i}.gif')

    addshape('res/campus/girl.gif')
    addshape('res/campus/boy.gif')

def init_turtles():
    tr_medicine.ht()
    tr_medicine.penup()
    tr_medicine.shape('res/medicines/medicine_0.gif')
    tr_medicine.goto(-199, -199)
    tr_medicine.st()

    tr_girl.ht()
    tr_girl.penup()
    tr_girl.shape('res/campus/girl.gif')
    tr_girl.goto(-160, 100)
    tr_girl.st()

    tr_boy.ht()
    tr_boy.penup()
    tr_boy.shape('res/campus/boy.gif')
    tr_boy.goto(-160, -100)
    tr_boy.st()


def tap(x, y):
    """Respond to screen tap."""
    
    
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10
        tr_medicine_degree = math.atan2(y+199,x+199)/math.pi*180
        tr_medicine.shape(f'res/medicines/medicine_{round(tr_medicine_degree/10)}.gif')


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for i, target in enumerate(targets):
        turtles[i].goto(target.x, target.y)
        

    if inside(ball):
        tr_medicine.goto(ball.x, ball.y)

    update()


def move():
    """Move ball and targets."""
    global total_virus, current_virus
    if randrange(10) == 0 and current_virus < total_virus:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

        tr = Turtle()
        tr.penup()
        tr.shape('res/virus.gif')
        tr.goto(target.x, target.y)
        turtles.append(tr)

        current_virus = current_virus + 1

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)


    for i, target in enumerate(targets):
        if abs(target - ball) < 30:
            del targets[i]
            turtles[i].ht()
            del turtles[i]
            break
            

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 10)


setup(420, 420, 370, 0)
add_shapes()
init_turtles()
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


