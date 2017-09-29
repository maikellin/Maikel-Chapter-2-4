import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
colors=["red","blue","violet","green","yellow","purple"]
for i in colors:
    print(i)
    alex.color(i)
    alex.forward(100)
    alex.left(60)