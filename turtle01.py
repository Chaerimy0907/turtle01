import turtle
import math

# 스크린 생성
s = turtle.getscreen()
s.setup(600,600)

# 장애물 생성 거북
ob=turtle.Turtle()
ob.hideturtle()
ob.penup()
ob.goto(-50,50)
ob.pendown()
ob.begin_fill()
for i in range(4):
    ob.forward(100)
    ob.right(90)
ob.end_fill()

# 출발/도착 지점 표시
st=turtle.Turtle()
st.hideturtle()
st.shape("circle")
st.shapesize(4)
st.penup()
st.goto(-200,-200)
st.showturtle()
st.color("blue", "white")
ed=turtle.Turtle()
ed.hideturtle()
ed.shape("circle")
ed.shapesize(4)
ed.penup()
ed.goto(200,200)
ed.showturtle()
ed.color("blue", "white")

# 거북이 변수 지정
turtle.shape("turtle")
turtle.penup()
turtle.goto(-200,-200)
turtle.showturtle()
turtle.pendown()

total_distance=0 # 누적된 거리
pre_x,pre_y=turtle.pos()

def cal_distance(x,y):
    global total_distance, pre_x, pre_y
    turtle.goto(x,y)
    new_x,new_y=x,y
    distance=math.sqrt((new_x-pre_x)**2 + (new_y-pre_y)**2)
    total_distance += distance
    pre_x,pre_y=new_x,new_y
    
turtle.left(45)
cal_distance(-70,-70)
turtle.left(40)
cal_distance(-70,70)
turtle.right(90)
cal_distance(70,70)
turtle.left(45)
cal_distance(200,200)

print(f"{total_distance}")
# # 장애물 회피 경로
# turtle.left(45)
# turtle.forward(180)
# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(180)