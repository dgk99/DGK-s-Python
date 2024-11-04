# 야구 게임
import random

# 컴퓨터가 생성한 3개의 난수를 저장할 리스트
com_list = []
# 3개의 난수가 저장됐나 확인하는 count변수 지정
count = 0
# 언제 중복이 안될지 모르니 while문 사용
while count < 3:
    # 컴퓨터가 0부터 9까지 중복되지 않은 3개의 난수 생성
    random_num = random.randint(0, 9)
    for i in range(count):
        if com_list[i] == random_num:
            break
    else:
        com_list.append(random_num)
        count += 1


# 게임 카운트, out 변수 생성
game_count = 1 # print에서 시도에 띄워줘야 하니까 1부터 시작
out = 0
# 사용자가 3개의 난수 입력
while True:
    # 사용자가 입력한 숫자를 저장할 리스트
    user_list = []
    for _ in range(3):
        user_input = int(input("0부터 9사이의 정수를 입력하세요: "))
        user_list.append(user_input)
    
    # 스트라이크, 볼 변수 생성
    strike, ball = 0, 0
    # 사용자 값과 컴퓨터 난수를 비교 후 스트라이크, 아웃 확인
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_list[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    
    print(com_list)
    
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")
    game_count += 1
    
    if strike == 0 and ball == 0:
        out += 1
        print(f"결과: {strike} Strike, {ball} Ball, {out} Out")
    else:
        print(f"결과: {strike} Strike, {ball} Ball")


    # 게임 패배 조건
    
    # 시도 횟수가 5회 이상이거나 스트라이크 아웃 2회 이상일 경우
    if game_count > 5:
        print("게임 종료: 패배 (시도 횟수 5회 초과)")
        break
    elif out >= 2:
        print("게임 종료: 패배 (스트라이크 아웃 2회)")
        break

    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수를 자리 순서대로 맞췄을 경우
    if strike == 3:
        print("게임 종료: 승리")
        break
