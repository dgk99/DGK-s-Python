import turtle

# .screen 하나의 창을 의미
screen = turtle.Screen()

# 그림을 그릴 거북이 객체 생성
t = turtle.Turtle()

# screen과 t는 참조 변수이다.
# 이 참조 변수를 호출하면, screen이라는 object가 만들어진다. object안에는 변수, 함수가 들어있다.
# 그리고, screen object의 주소값을 불러온다.

# 그림을 그리려면 종이와 펜이 필요한데,
# 종이가 screen, 펜은 t가 된다.

# 거북이의 이동속도를 나타냄.(1~10)
t.speed(1)

# 거북이를 앞으로 100 이동시킨다. (100의 단위는 픽셀)
t.forward(100)

# 거북이를 오른쪽으로 90도로 회전
t.right(90)

# 거북이를 뒤로 200만큼 이동
t.backward(200)

# 거북이를 왼쪽으로 270도 회전
t.left(270)

# 펜을 들어 그림을 그리지 않도록 함
t.penup()

# 거북이를 초기 위치로 이동
t.home()

# 펜을 내려서 그림을 그리도록 함
t.pendown()

#거북이를 왼쪽으로 90도 회전시킴
t.left(90)

#거북이를 앞으로 100만큼 이동시킴
t.forward(100)

# 터틀 그래픽 창이 닫히지 않고 유지되도록 함
turtle.done()
