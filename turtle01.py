import turtle

# 스크린 생성
s = turtle.getscreen()
s.setup(600,600)

# 장애물 생성 거북
ob=turtle.Turtle()
ob.shape("square")
ob.shapesize(6,6)

# 출발/도착 지점 표
turtle.color("blue")
turtle.hideturtle()
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.showturtle()
turtle.color("black")


# 거북이 변수 지정
turtle.shape("turtle")
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.goto(200,200)

