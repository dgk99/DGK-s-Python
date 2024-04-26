# 사용자로부터 "left", "right", "up", "down"중 하나의 단어를 입력받는다.
direction = input("방향을 입력하세요(left, right, up, down): ")

# 사용자가 "left"라고 입력했다면 왼쪽으로 이동합니다. 라고 출력한다.
if direction == "left":
    print("왼쪽으로 이동합니다.")
    
# 사용자가 "right"라고 입력했다면 오른쪽으로 이동합니다. 라고 출력한다.
elif direction == "right":
    print("오른쪽으로 이동합니다.")
    
# 사용자가 "up"라고 입력했다면 위로 이동합니다. 라고 출력한다.
elif direction == "up":
    print("위로 이동합니다.")
    
# 사용자가 "down"라고 입력했다면 아래로 이동합니다. 라고 출력한다.
elif direction == "down":
    print("아래로 이동합니다.")
    
# 사용자가 보기와 다른 단어를 입력한다면 알 수 없는 명령입니다. 라고 출력한다
else:
    print("알 수 없는 명령입니다.")