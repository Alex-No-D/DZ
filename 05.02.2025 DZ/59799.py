from turtle import *
screensize(1000,1000)
shape('turtle')
tracer(0)
k = 20
left(90)
for i in range(2):
    forward(9*k)
    right(90)
    forward(15*k)
    right(90)
penup()
forward(12*k)
right(90)
pendown()
for i in range(2):
    forward(6*k)
    right(90)
    forward(12*k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x* k, y*k)
        dot(3, 'red')
done()