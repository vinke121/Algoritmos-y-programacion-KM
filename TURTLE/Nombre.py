import turtle
import colorsys

nombre = turtle.Turtle()
turtle.title("Mi Nombre")
turtle.bgcolor("black")
h=0
for i in range(100):
   c = colorsys.hsv_to_rgb(h, 1, 1)
   nombre.speed(0)
   nombre.pencolor(c)
   nombre.circle(i)   
   nombre.right(30)
   h = h+0.005


#moverme con cordenadas(goto) y en angulos(setheading)
nombre.pencolor("red")
nombre.pensize(6)
nombre.speed(1)

#Primer Nombre
#K
nombre.penup()
nombre.goto(-300,-100)
nombre.pendown()
nombre.setheading(90)
nombre.goto(-300,70)
nombre.penup()
nombre.goto(-300,0)
nombre.pendown()
nombre.goto(-250,70)
nombre.penup()
nombre.goto(-300,0)
nombre.pendown()
nombre.goto(-250,-100)



#E
nombre.penup()
nombre.goto(-170,-100)
nombre.pendown()
nombre.goto(-230,-100)
nombre.goto(-230,0)
nombre.goto(-170,0)
nombre.goto(-170,-50)
nombre.goto(-230,-50)


#V
nombre.penup()
nombre.goto(-150,0)
nombre.pendown()
nombre.goto(-110,-100)
nombre.goto(-70,0)


#I
nombre.penup()
nombre.goto(-60,-100)
nombre.pendown()
nombre.goto(-60,0)
nombre.penup()
nombre.goto(-60,10)
nombre.pendown
nombre.dot(7, "purple")


#N
nombre.penup()
nombre.goto(-40,-100)
nombre.pendown()
nombre.goto(-40,0)
nombre.penup()
nombre.goto(-40,-5)
nombre.pendown()
nombre.goto(20,-5)
nombre.goto(20,-100)

#segundo Nombre
#A

nombre.penup()
nombre.goto(80,-100)
nombre.pendown()
nombre.goto(120,70)
nombre.goto(160,-100)
nombre.penup()
nombre.goto(105,0)
nombre.pendown()
nombre.goto(135,0)

#n
nombre.penup()
nombre.goto(170,-100)
nombre.pendown()
nombre.goto(170,0)
nombre.penup()
nombre.goto(170,-5)
nombre.pendown()
nombre.goto(230,-5)
nombre.goto(230,-100)

#d
nombre.penup()
nombre.goto(300,-100)
nombre.pendown()
nombre.goto(300,70)
nombre.penup()
nombre.goto(300,-100)
nombre.pendown()
nombre.goto(240,-100)
nombre.goto(240,0)
nombre.goto(300,0)

#r
nombre.penup()
nombre.goto(310,-100)
nombre.pendown()
nombre.goto(310,0)
nombre.pendown()
nombre.goto(310,-20)
nombre.goto(330,-10)
nombre.goto(335,0)

#e
nombre.penup()
nombre.goto(395,-100)
nombre.pendown()
nombre.goto(345,-100)
nombre.goto(345,0)
nombre.goto(395,0)
nombre.goto(395,-50)
nombre.goto(345,-50)

#s
nombre.penup()
nombre.goto(405,-100)
nombre.pendown()
nombre.goto(445,-100)
nombre.goto(445,-50)
nombre.goto(405,-50)
nombre.goto(405,0)
nombre.goto(445,0)
   
turtle.done()