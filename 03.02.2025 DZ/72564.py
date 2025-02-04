from turtle import *
screensize(1000,1000)
shape('turtle')
tracer(0)
left(90)
k = 20
for i in range(2):
    forward(23*k)
    right(90)
    forward(10*k)
    right(90)
forward(3*k)
left(90)
forward(12*k)
right(90)
for i in range(2):
    forward(9*k)
    right(90)
    forward(32*k)
    right(90)
penup()
for x in range(-35,35):
    for y in range(-35,35):
        goto(x*k,y*k)
        dot(3, 'red')




done()