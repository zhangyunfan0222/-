from random import randrange
from turtle import *
from utils import vector
import math


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
turtles = []

total_virus = 100
current_virus = 0
kill_virus = 0

tr_medicine = Turtle()
tr_medicine_degree = 0.0
tr_girl = Turtle()
tr_boy = Turtle()
tr_status = Turtle()
tr_final  = Turtle()

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

    tr_status.ht()
    tr_status.penup()
    tr_status.goto(-100, -199)

    tr_final.ht()
    tr_final.penup()
    tr_final.goto(-190, 0)


def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10
        tr_medicine_degree = math.atan2(y+199,x+199)/math.pi*180
        tr_medicine.shape(f'res/medicines/medicine_{round(tr_medicine_degree/10)}.gif')


def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    clear()

    for i, target in enumerate(targets):
        turtles[i].goto(target.x, target.y)
        

    if inside(ball):
        tr_medicine.goto(ball.x, ball.y)

    tr_status.clear()
    tr_status.write(f"打败新冠病毒:{kill_virus}, 剩下新冠病毒：{total_virus - kill_virus}")

    if kill_virus == total_virus:
        tr_final.clear()
        tr_final.color("#c69320")
        tr_final.write(f"战胜新冠病毒，胜利！", font=('Arial', 26, 'bold'))
        
    update()

def move():
    global total_virus, current_virus, kill_virus
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
            kill_virus = kill_virus + 1
            break
            
    draw()

    for target in targets:
        if not inside(target):
            tr_final.clear()
            tr_final.color("#990f02")
            tr_final.write(f"已被感染，请马上治疗！", font=('Arial', 26, 'bold'))
            return

    ontimer(move, 10)


setup(420, 420, 370, 0)
title("战胜新冠 1.0")
add_shapes()
init_turtles()
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


