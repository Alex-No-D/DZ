from turtle import *
tracer(0)
screensize(400,400)
shape('turtle')
pendown()
left(90)
k = 20
for i in range(6):
    right(36)
    forward(10*k)
    right(36)

penup()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*k,y*k)
        dot(3,'red')
done()