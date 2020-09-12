#PythonDraw.py
import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ("yellow","blue","orange","green","purple","red")
for i in range(300):
    turtle.fd(1.1*i)
    turtle.color(colors[i % 6])
    turtle.left(61)
turtle.done
