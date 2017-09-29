import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
sides = int(input("How many sides? "))
length = int(input("How long should each side be? "))

for i in range(10):
    alex.forward(100)
    alex.left(360/10)
    