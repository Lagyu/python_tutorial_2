import turtle


kame = turtle.Turtle()
kame.speed(10)
while True:
    kame.forward(200)
    kame.left(179)
    if abs(kame.pos()) < 1:
        break
kame.end_fill()



