from turtle import *
screensize(1000,1000)
shape('turtle')
tracer(0)
k = 10
left(90)

for i in range(4):
    forward(28*k)
    right(90)
    forward(26*k)
    right(90)
penup()
forward(8*k)
right(90)
forward(7*k)
left(90)
pendown()
for i in range(4):
    forward(67*k)
    right(90)
    forward(98*k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x* k, y*k)
        dot(3, 'red')
done()