import turtle

# 스크린 생성
s = turtle.getscreen()
s.setup(600,600)

# 장애물 생성 거북
ob=turtle.Turtle()
ob.shape("square")
ob.shapesize(5,5)

# 출발/도착 지점 표시
#turtle.color("blue")
#turtle.hideturtle()
#turtle.penup()
#turtle.goto(-200,-240)
#turtle.pendown()
#turtle.circle(40)
#turtle.penup()
#turtle.goto(200,160)
#turtle.pendown()
#turtle.circle(40)
#turtle.penup()
#turtle.color("black")
start=turtle.Turtle()
start.hideturtle()
start.shape("circle")
start.shapesize(4)
start.penup()
start.goto(-200,-200)
start.showturtle()
start.color("blue", "white")



# 거북이 변수 지정
turtle.shape("turtle")
turtle.penup()
turtle.goto(-200,-200)
turtle.showturtle()
turtle.pendown()

# 장애물 회피 경
turtle.left(45)
turtle.forward(180)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(180)
