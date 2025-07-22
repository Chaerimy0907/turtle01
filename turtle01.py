import turtle

# 스크린 생성
s = turtle.getscreen()
s.setup(600,600)

# 거북이 변수 지정
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(-200,-200)
t.pendown()
t.goto(200,200)