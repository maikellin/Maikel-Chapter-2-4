import turtle
wn=turtle.Screen()
alex=turtle.Turtle()
colors=["red","orange","blue","violet","green","yellow","purple","brown"]
for i in colors:
    print(i)
    alex.color(i)
    alex.forward(100)
    alex.left(45)