#------------------------------------------------------------------------------------------------------
#Assingment2A - CIS187 - Phillip Leman
#
#Purpose: The purpose of this program is to use the python turtle library to create a series of shapes. 
#
#Author: Phillip Leman
#created: February 01, 2021
#
#
#------------------------------------------------------------------------------------------------------


import turtle

#Window_setup
sc = turtle.Screen()
sc.setup(500, 500)
sc.bgcolor("#FFFFCC")

def draw_circle(turtle, color, size, x, y):
   
    turtle.color(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.hideturtle()

circle = turtle.Turtle()

#Aqua Circle
draw_circle(circle, "aqua", 80, 10, 0)

#Purple Circle
draw_circle(circle, "purple", 60, 30, -120)

#Green Circle
draw_circle(circle, "green", 40, 128, -83)

#Red Circle
draw_circle(circle, "red", 20, 111, -1)

#################################

#Colored Lines
#Aqua Turtle
aql = turtle.Turtle()
aql.color("aqua")
aql.shape("square")
aql.penup()
aql.goto(90,90)
#Aqua Line
aqll = turtle.Turtle()
aqll.color("aqua")
aqll.hideturtle()
aqll.penup()
aqll.goto(90,90)
aqll.pendown()
aqll.goto(90,0)

#Purple/Red Line
ppl = turtle.Turtle()
ppl.color("purple")
ppl.hideturtle()
ppl.penup()
ppl.goto(25,0)
ppl.pendown()
ppl.forward(65)
ppl.color("red")
ppl.shape("turtle")
ppl.forward(19)
ppl.showturtle()

#Green Line/Circle
grt = turtle.Turtle()
grt.penup()
grt.goto(25,0)
grt.color("green")
grt.forward(65)
grt.pendown()
grt.shape("circle")
grt.goto(90, -40)







turtle.done()