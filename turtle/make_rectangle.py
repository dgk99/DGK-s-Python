import turtle

# #종이 만들기
# screen = turtle.Screen()

# # 거북이 부르기
# t = turtle.Turtle()

# # 거북이 속도 정하기(3으로 해보자)
# t.speed(3)

# # home에서 앞으로 100 이동
# t.forward(100)

# # 왼쪽으로 90도 이동
# t.left(90)

# # 앞으로 50이동
# t.forward(50)

# # 오른쪽으로 90도 이동
# t.right(90)

# # 뒤로 100이동
# t.backward(100)

# # 오른쪽으로 90도 이동
# t.right(90)

# # 앞으로 50이동
# t.forward(50)

# # 펜 들기
# t.penup

# # 터틀 종료
# turtle.done()

#----------------------------------

# 수업 자료에 있는 for문을 사용하는 방법

# 종이 생성
screen = turtle.Screen()
# 거북이 생성
t = turtle.Turtle()
# 두 번 반복하여 직사각형을 그림
for _ in range(2) :
    # 거북이를 앞으로 100 이동
    t.forward(100)
    # 거북이를 오른쪽으로 90 회전
    t.right(90)
    # 거북이를 앞으로 50 이동
    t.forward(50)
    # 거북이를 오른쪽으로 90 회전
    t.right(90)
    
# 거북이 놓아주기
turtle.done()
