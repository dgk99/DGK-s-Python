# 야구 게임

# 난수 저장 리스트
import random

com_list = []
#  게임 규칙
while len(com_list) < 3:
    # 1. 컴퓨터 난수 생성
    # • 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
    random_num = random.randint(0, 9)
    for i in range(len(com_list)):
        if com_list[i] == random_num:
            break
    else:
        com_list.append(random_num)
print(com_list)

# 게임 횟수, 아웃 카운트
game_count = 1
o = 0
# 조건을 만족할 때 까지 반복
while True:
    # 2. 플레이어 입력
    # • 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
    user_input = input(f"시도 {game_count}: 입력한 숫자 - ").split()

    # • 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
    
    # 스트라이크, 볼 카운트
    s, b = 0, 0
    
    # 스트라이크, 볼 판정
    for i in range(3):
        for j in range(3):
            if com_list[i] == int(user_input[j]):
                if i == j:
                    s += 1
                else:
                    b += 1
    if s == 0 and b == 0:
        o += 1
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    else:
        print(f"결과: {s} Strike, {b} Ball")
        
    # 4. 게임 승리 조건
    # • 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.
    if s == 3:
        print(f"게임 종료: 승리\n정답: {user_input[0]} {user_input[1]} {user_input[2]}")
        break
    # 3. 게임 패배 조건
    # • 시도 횟수가 5번 이상일 경우.
    elif game_count >= 5:
        print(f"게임 종료: 패배 (게임 시도 횟수 5회 초과)\n정답: {user_input[0]} {user_input[1]} {user_input[2]}")
        break
    # • 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
    elif o == 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 초과)\n정답: {user_input[0]} {user_input[1]} {user_input[2]}")
        break
    game_count += 1