import turtle

tur = turtle.Turtle()
tur.speed(100)


def sqr():

    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)


#sqr()
#ur.forward(200)
#sqr()
#turtle.left(45)
#turtle.forward(20)

for x in range(4):
    sqr()
tur.forward(200)
for x in range(4):
  sqr()
