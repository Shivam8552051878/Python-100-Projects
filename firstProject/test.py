import turtle
a = turtle.Turtle()      #instantiate a new turtle object called 'a'
# a.hideturtle()           #make the turtle invisible
a.penup()                #don't draw when turtle moves
a.goto(-200, -200)       #move the turtle to a location
a.showturtle()           #make the turtle visible
a.pendown()              #draw when the turtle moves
# a.goto(50, 50)
a.forward(50)
turtle.Screen().exitonclick()