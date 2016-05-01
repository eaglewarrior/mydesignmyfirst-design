import turtle
def draw_square(some_turtle):
    for i in range(1,5):
	    some_turtle.forward(100)
	    some_turtle.right(90)
	
def draw_rhombus(some_turtle):
    for i in range(1,3):
	    some_turtle.forward(150)
	    some_turtle.left(45)
	    some_turtle.forward(100)
	    some_turtle.left(135)
	
def draw_circle(circle,radius,color):
    circle.color(color)
    circle.circle(radius)
		
def draw_turtles():
    window=turtle.Screen()
    window.bgcolor("black")
	
    squ=turtle.Turtle()
    squ.shape("turtle")
    squ.color("yellow")
    squ.speed(100)
    for i in range(1,37):
        draw_square(squ)
        squ.right(10)
    cir=turtle.Turtle()
    cir.speed(100)
    cir.shape("circle")
    cir.color("blue")
    for i in range (1,11):
        cir.circle(50)
        cir.right(36)
    rob=turtle.Turtle()
    rob.shape("arrow")
    rob.color("orange")
    rob.speed(100)
    for i in range(1,37):
        draw_rhombus(rob)
        rob.right(10)
    flower=turtle.Turtle()
    flower.speed(100)
    flower.shape("arrow")
    flower.right(45)
    for i in range(1,37):
        for j in range(1,5):
            draw_circle(flower,i,"green")
            flower.left(90)
            flower.right(45)
    flower.color("green")
    flower.forward(200)
	

    window.exitonclick()
	
draw_turtles()
	
