# 삼각형 만들기
import turtle

# 종이 생성
# screen = turtle.Screen()

# # 거북이 부르기
# t = turtle.Turtle()

# # 거북이 속도 지정(이번엔 빠르게 5)
# t.speed(5)

# # 앞으로 100 이동
# t.forward(100)

# # 왼쪽으로 90도 회전
# t.left(90)

# # 앞으로 100 이동
# t.forward(100)

# # 집으로 거북이 이동하면서 그림
# t.home()

# # 펜 들기
# t.penup

# # 터틀 종료
# turtle.done()

#------------------------------

# 수업 자료에 나와있는 for 반복문 사용

# 종이 생성
screen = turtle.Screen()
# 거북이 부르기
t = turtle.Turtle()
# 세 번 반복하여 삼각형 그림
for _ in range(3) :
    # 거북이를 앞으로 100 이동
    t.forward(100)
    # 거북이를 왼쪽으로 120도 회전
    t.left(120)
# 거북이 놓아주기
turtle.done()