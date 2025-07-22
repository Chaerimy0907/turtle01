import turtle
import math
import random

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

# 출발 지점 표시
st=turtle.Turtle()
st.hideturtle()
st.penup()
st.goto(-200,-200)
st.shape("circle")
st.shapesize(2)
st.showturtle()
st.color("blue", "white")
stw=turtle.Turtle()
stw.hideturtle()
stw.penup()
stw.goto(-200,-170)
stw.write("START",align="center",font=("Arial",20,"bold"))


# 도착 지점 표시
ed=turtle.Turtle()
ed.hideturtle()
ed.penup()
ed.goto(200,200)
ed.shape("circle")
ed.shapesize(2)
ed.showturtle()
ed.color("red", "white")
edw=turtle.Turtle()
edw.hideturtle()
edw.penup()
edw.goto(200,230)
edw.write("GOAL",align="center",font=("Arial",20,"bold"))

# 거북이 변수 지정
player=turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(-200,-200)
player.setheading(player.towards(200,200))
player.pendown()

total_distance=0 # 누적된 거리
pre_x,pre_y=player.pos()

# 거리 계산 함수
def update_distance():
    global total_distance, pre_x, pre_y
    new_x,new_y=player.pos()
    d=math.sqrt((new_x-pre_x)**2 + (new_y-pre_y)**2)
    total_distance += d
    pre_x,pre_y=new_x,new_y

# 충돌 감지 함수
def check_collision():
    # 현재 거북이의 위치 가져오기
    player_x=player.xcor()
    player_y=player.ycor()
        
    # 충돌 판정 : turtle의 외곽이 장애물과 겹치는지 확
    if -60 <= player_x <= 60 and -60 <= player_y <= 60:
        return True # 충돌발
    return False # 안전

# 회피 함수
def avoid_obstacle():
    # 현재 방향을 기준으로 좌우 90도씩 체크
    current_heading=player.heading()
    
    directions=[90,-90] #좌우(90도 회전) 중 선택
    random.shuffle(directions) #좌우 방향을 무작위로 섞음
    
    for angle in directions:
        #새로운 방향 계산 : 현재 방향에서 좌/우로 꺾은 각도
        new_heading=current_heading+angle
        
        #꺾은 방향으로 50픽셀 이동했을 때의 가상 좌표 계산
        test_x=player.xcor()+50*math.cos(math.radians(new_heading))
        test_y=player.ycor()+50*math.sin(math.radians(new_heading))
        
        # 그 좌표가 장애물 범위 밖이라면 -> 그 방향으로 회피 가능
        if not (-60<=test_x<=60 and -60<=test_y<=60):
            player.setheading(new_heading) # 해당 방향으로 머리를 돌림
            player.forward(40) # 앞으로 이동
            update_distance()
            return
        
    # 좌우 둘 다 막혔을 경우 -> 뒤로 후진(180도 회전)
    player.setheading(current_heading+180)
    player.forward(40)
    update_distance()

def move_towards_goal():
    player.setheading(player.towards(200,200))
    player.forward(10)
    update_distance()
    
def game_loop():
    step=0
    while player.distance(200,200)>10 and step<1000:
        # 1. 충돌 확인
        if check_collision():
            print(f"Step {step} : 장애물 감지!")
            avoid_obstacle()
        else:
            # 2. 평상시 이동
            move_towards_goal()  
        step += 1
        s.update()
    
    text=turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(0,200)
    text.write(f"              도착!\n총 이동 거리 : {round(total_distance,2)}px",align="center",font=("Arial",20,"bold"))
    print("도착!")
    print(f"총 이동 거리 : {round(total_distance,2)}px")
    
game_loop()
turtle.done()