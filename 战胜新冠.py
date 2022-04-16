# 1. 安装freegames,  pip install freegames
# 2. 选择Cannon游戏作为模板
#        https://grantjenks.com/docs/freegames/#cannon
# 3. 添加新冠病毒图片
#

from random import randrange
from turtle import *
from freegames import vector


wn = Screen()
wn.addshape('res/virus.gif')


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
turtles = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for i, target in enumerate(targets):
        turtles[i].goto(target.x, target.y)
        

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

        tr = Turtle()
        tr.penup()
        tr.shape('res/virus.gif')
        tr.goto(target.x, target.y)
        turtles.append(tr)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    print(targets)


    for i, target in enumerate(targets):
        if abs(target - ball) < 20:
            del targets[i]
            turtles[i].ht()
            del turtles[i]
            break
            

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


