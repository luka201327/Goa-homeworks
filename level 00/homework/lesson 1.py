from turtle import  *


#WE WANT TO PAINT  A  HOUSE
speed(7)
#STEP 1 : DRAW A SQUARE
width(7)  

color("PURPLE")

forward (200)   



left(90)




forward(200)
 
left(90)
forward(200)
left(90)
forward(200)

left(90)
color("PURPLE")
 

begin_fill()
forward(70)  
color("YELLOW")
left(90)
forward(129)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown() 
begin_fill()
color("RED")

right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
penup()
goto(150,150)
pendown()
left(30)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
begin_fill()
penup()
goto(50,150)
left(90) 
pendown()
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
exitonclick()