import turtle

side=300

turtle.right(180)
for i in range(12):
    turtle.forward(side-(25*i))
    turtle.left(90)

turtle.exitonclick()