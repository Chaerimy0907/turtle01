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

# 충돌 감지 함수
def check_collision():
    # 현재 거북이의 위치 가져오기
    turtle_x=turtle.xcor()
    turtle_y=turtle.ycor()
    
    # 정사각형 장애물 중심 : (0,0), 변의 길이 50 -> 좌우 +-25, 상하 +-25
    box_half=25
    radius=10
        
    # 충돌 판정 : 거북이 크기 + 장애물 반지름
    if (-(box_half+radius) < turtle_x < (box_half+radius)) and (-(box_half+radius) < turtle_y < (box_half+radius)):
        return True # 충돌발생
    return False # 안전

# 거리 계산 함수
def cal_distance(x,y):
    global total_distance, pre_x, pre_y
    turtle.goto(x,y)
    new_x,new_y=x,y
    d=math.sqrt((new_x-pre_x)**2 + (new_y-pre_y)**2)
    total_distance += d
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

if turtle.pos()==(200,200):
    print("Goal")

