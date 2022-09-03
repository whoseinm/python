from turtle import*

bgcolor("black")
pensize(3)
speed(0)
hideturtle()
for i in range(240):
    for colors in ["red","blue","green","white","orange","pink","purple",]:
        color(colors)
        circle(100)
        left(10)

done()