# 방향 명령어 해석기

# 사용자로부터 "left", "right", "up", "down" 중 하나의 단어를 입력받습니다.
direction = input("방향을 입력하세요(left, right, up, down): ")
# 입력받은 문자열에 따라 "왼쪽으로 이동합니다"
if direction == "left" :
    print("왼쪽으로 이동합니다.")
# "오른쪽으로 이동합니다."
elif direction == "right" :
    print("오른으로 이동합니다.")
# "위로 이동합니다"
elif direction == "up" :
    print("위로 이동합니다.")
# "아래로 이동합니다"
elif direction == "down" :
    print("아래로 이동합니다.")
# 를 출력합니다.
# 만약 다른 단어가 입력되면, "알 수 없는 명령입니다"를 출력하세요
else:
    print("알 수 없는 명령입니다.")