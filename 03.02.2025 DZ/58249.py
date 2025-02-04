from turtle import *
tracer(0)
screensize(400,400)
shape('turtle')
pendown()
left(90)
k = 20
for i in range(5):
    right(90)
    circle(5 * k, 180)
    right(90)
    circle(5 * k, 180)
    right(90)
    circle(5 * k, 180)
    right(90)
    circle(5 * k, 180)

penup()
for x in range(-100,100):
    for y in range(-100, 100):
        goto(x*k,y*k)
        dot(3,'red')
done()