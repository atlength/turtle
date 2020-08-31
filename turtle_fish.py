import turtle
import time

pen=turtle.Pen()
pen.ht()
pen.width(2)
pen.speed(0)

def fish(x=0,y=0,rd=100,hd=0):
    pen.up()
    pen.setpos(x,y)
    pen.seth(-hd)
    pen.circle(rd/2,180)
    pen.down()
    #white fish
    pen.circle(rd,180)
    #black fish
    pen.begin_fill()
    pen.fillcolor('black')
    pen.circle(rd,180)
    pen.seth(pen.heading()-180)
    pen.circle(-rd/2,180)
    pen.circle(rd/2,180)
    pen.end_fill()
    #fishes' eyes
    pen.up()
    pen.circle(rd/4+rd/20,180)
    pen.begin_fill()
    pen.fillcolor('white')
    pen.circle(rd/10)
    pen.end_fill()
    pen.circle(-rd/2+rd/10,180)
    pen.begin_fill()
    pen.fillcolor('black')
    pen.circle(rd/10)
    pen.end_fill()

while True:
    for i in range(10):
        pen.clear()
        fish(rd=200,hd=i*36)
        time.sleep(0.5)


