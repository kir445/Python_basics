import turtle 
#here screen() is a method
wn=turtle.Screen()
wn.bgcolor("yellow")
arr=turtle.Turtle()
arr.color("red")
arr.forward(120)
#wheels
def wheels():
 k=40
 while k<56:
   arr.backward(20)
   arr.right(90)
   arr.left(40)
   arr.forward(10)
   k=k+1

 arr.up()
 arr.goto(-15,-10)
 arr.down()
 while k<70:
   arr.backward(20)
   arr.right(90)
   arr.left(40)
   arr.forward(10)
   k=k+1
wheels()
arr.up()
arr.color("blue")
arr.goto(120,80)
arr.down()
def triangle():
 arr.backward(50)
 arr.left(45)
 arr.forward(40)
 arr.right(95)
 arr.forward(40)
triangle()
arr.up()
arr.goto(80,40)
arr.down()
arr.color("pink")
p=20
for p in range(55):
  arr.forward(p)
  arr.left(15)
  arr.backward(12)
  arr.right(30)
  p=p+12
arr.up()  
arr.goto(80,140)
arr.down()
arr.left(15)
arr.forward(40)




