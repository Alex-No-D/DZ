from turtle import *
screensize(1000,1000)
shape('turtle')
tracer(0)
k = 20
left(90)

for i in range(4):
    forward(5*k)
    right(90)
    forward(10*k)
    right(90)

penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x* k, y*k)
        dot(3, 'red')
done()