import turtle


t = turtle.Pen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

turtle.bgcolor('black')
for i in range(360):
    t.pencolor(colors[i%6])
    t.width(i/100 + 1) 
    t.forward(i) 
    t.left(59) 
