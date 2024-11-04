# 야구 게임

# 컴퓨터 난수 생성
# 난수 저장할 리스트
import random


com_list = []
# 저장된 난수를 나타내주는 count 생성
count = 0
# 중복 되지 않는 정수 3개가 저장될 때 까지 반복해야 하니 while문에 조건문 사용
while count < 3:
    # 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성
    # 난수 생성
    word_random = random.randint(0, 9)
    # 중복값 검사
    for index in range(count):
        if word_random == com_list[index]:
            break
    else:
        com_list.append(word_random)
        count += 1
print(com_list)

# 게임 횟수, 아웃 카운트 생성
game_count = 1
o = 0

# 게임 승리, 패배 조건을 만족할 때 까지 반복해야 하니 while문 사용
while True:
    # 플레이어 입력
    # 플레이어 입력 값 저장할 리스트
    user_list = []
    # 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력
    for i in range(3):
        user_input = int(input("0~9 사이의 정수를 하나 입력하세요: "))
        user_list.append(user_input)
    print(user_list)
    
    # 스트라이크, 볼 카운트
    s = 0
    b = 0
    
    # 스트라이크, 볼 판별
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_list[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
                    
    # 시도, 입력한 숫자 출력
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")

    # 결과 출력
    if s == 0 and b == 0:
        o += 1
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    else:
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    
    # 게임 패배 조건
    # 시도 횟수가 5번 이상
    if game_count >= 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 초과)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    # 스트라이크 아웃 횟수 2번 이상
    elif o >= 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 이상)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    if s == 3:
        print(f"게임 종료: 승리\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    
    game_count += 1