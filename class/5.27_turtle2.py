import random
import turtle

# 화면을 설정합니다.
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width() // 2
height = screen.window_height() // 2

print(width, height)

# 거북이를 생성합니다.
t = turtle.Turtle()

# 거북이가 움직이는 함수를 정의합니다.
def move_forward():
    t.forward(100)
    
    x, y = t.position()
    if x >= width or x <= -width or y >= height or y <= -height :
        t.left(180)
    
def move_backward():
    t.backward(100)
    
    
def turn_left():
    t.left(15)
    
def turn_right():
    t.right(15)
    
# 펜 색깔을 검은색으로 변경 -> "b" Key를 누를 때 호출
def change_color_to_black():
    t.pencolor("black")
    
# 펜 색깔을 빨간색으로 변경 -> "r" Key를 누를 때 호출
def change_color_to_red():
    t.pencolor("red")
    
# 검은색이면 빨간색, 빨간색이면 검은색으로 변경 -> "i" Key를 누를 때 호출
# def change_color_to_opposition():
#     if t.pencolor() == "black":
#         t.pencolor("red") 
#     else:
#         t.pencolor("black")    

def inverse_color():
    current_pen_color = t.pencolor()
    
    if current_pen_color == "red":
        t.pencolor("black")
    # if를 써도 되지만, 둘 중에 하나를 선택한다는게 명확히 보이기 때문  
    elif current_pen_color == "black" :
        t.pencolor("red")
    
    
def change_color():
    
    print("색깔 선택: ")
    print("1. 파란색")
    print("2. 검정색")
    print("3. 노란색")
    # 1 ~ 3 이외 값 입력 시 재입력 -> 언제까지? 1~3 값이 입력 될 때 까지
    # while True:
    #     input_value = int(input("숫자 입력: "))
        
    #     # 아래 if문이 1~3이하의 숫자이면, 실행된다.
    #     # 중첩 if문
    #     if 1 <= input_value <= 3 :
    #         if input_value == 1 :
    #             t.pencolor("blue") 
    #         elif input_value == 2 :
    #             t.pencolor("black") 
    #         elif input_value == 3 :
    #             t.pencolor("yellow")
    #         break
    #     else:
    #         print("잘못된 입력입니다. 다시 입력해 주세요")
    
    while not (1 <= input_value <= 3):
        input_value = int(input("숫자 입력: "))
    if input_value == 1 :
        t.pencolor("blue") 
    elif input_value == 2 :
        t.pencolor("black") 
    elif input_value == 3 :
        t.pencolor("yellow")
            
    
# 펜 색깔 변경 함수를 정의
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))
    
# 키보드 이벤트를 설정합니다.
screen.listen()
screen.onkey(move_forward, "Up") # 위쪽 화살표 키를 누르면 앞으로 이동
screen.onkey(move_backward, "Down") # 아래쪽 화살표 키를 누르면 뒤로 이동
screen.onkey(turn_left, "Left") # 왼쪽 화살표 키를 누르면 왼쪽으로 회전
screen.onkey(turn_right, "Right") # 오른쪽 화살표 키를 누르면 오른쪽으로 회전
screen.onkey(move_random, "c") # 'c' 키를 누르면 펜 색깔 변화
screen.onkey(change_color_to_black, "b")
screen.onkey(change_color_to_red, "r")
screen.onkey(change_color, "z")
# i를 누르면 색깔이 빨 -> 검 또는 검 -> 빨 로 반전
# 현재 펜 색깔이 빨간색 또는 검은색인 경우에만 반전

# screen.onkey(change_color_to_opposition, "i")


# 이벤트 루프를 시작합니다.
screen.mainloop()

