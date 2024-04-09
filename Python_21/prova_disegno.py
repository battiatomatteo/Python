import turtle

t=turtle.Turtle()
g=turtle.Screen()

g.bgcolor('black')
t.width(2)
t.speed(240)

col=('yellow', 'green','red', 'blue')

for i in range (300):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(137)