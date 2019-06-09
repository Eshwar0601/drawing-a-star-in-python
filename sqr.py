import turtle


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('coded by Eshwar')
squad = turtle.Turtle()
squad.color('white')


def draw(size):
    for i in range(10):
        squad.fd(size)
        squad.left(90)
        size -= 11



draw(146)
draw(136)
draw(126)
draw(116)
draw(106)
draw(96)
draw(86)

