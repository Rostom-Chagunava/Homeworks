from turtle import *










speed(10)
width(7)

color("purple")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90) 
# drawing a door
forward(70) 
color("yellow") 
begin_fill()
left(90) 
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(0,90)
pendown()
color("red")
begin_fill()
left(120)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
penup()
goto(200,90)
pendown()
color("red")
begin_fill()
right(0)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()




exitonclick()