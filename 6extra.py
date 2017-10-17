import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
res1=sides = int(input("How many sides? "))
res2=length = int(input("How long should each side be? "))
n=int(res1)
s=int(res2)

for i in range(n):
    alex.forward(100)
    alex.left(360/n)
    