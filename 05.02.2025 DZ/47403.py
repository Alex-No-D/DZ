from turtle import *
screensize(1000,1000)
shape('turtle')
tracer(0)
left(90)
k = 20
for i in range(4):
    forward(12*k)
    right(90)
right(30)
for i in range(3):
    forward(8*k)
    right(60)
    forward(8*k)
    right(120)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,'red')
done()