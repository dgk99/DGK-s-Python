# 야구 게임
# • 게임 규칙
# 1. 컴퓨터 난수 생성
# • 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
# 중복 값이 저장될 리스트
import random

com_list = []
# 리스트에 저장된 중복 값 확인하는 카운트
count = 0
# 난수 값이 3개 저장될 때 까지 반복
while count < 3:
    random_num = random.randint(0, 9)
    for i in range(count):
        if com_list[i] == random_num:
            break
    else:
        com_list.append(random_num)
        count += 1
print(com_list)

# 게임 횟수, 아웃 카운트
game_count = 1
o = 0

# 2. 플레이어 입력
# 승리, 패배 조건에 해당할 때 까지 반복
while True:
    # 유저 입력 값 리스트
    user_list = []
    # • 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
    for _ in range(3):
        # • 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
        user_input = int(input("0~9 사이의 정수를 입력하세요: "))
        user_list.append(user_input)
    
    
    # 시도 횟수, 입력한 숫자 출력
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")
    
    # 스트라이크, 볼 카운트
    s, b = 0, 0
    
    # 스트라이크, 볼 확인
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_list[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
    # 스트라이크, 볼이 없다면 아웃 카운트 증가
    if s == 0 and b == 0:
        o += 1
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    # 있다면 스트라이크, 볼 출력
    else:
        print(f"결과: {s} Strike, {b} Ball")

    # 3. 게임 패배 조건
    # • 시도 횟수가 5번 이상일 경우.
    if s == 3:
        print(f"게임 종료: 승리\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    
    if game_count >= 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 초과)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    # • 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
    elif o >= 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 이상)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    # 4. 게임 승리 조건
    # • 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.
    
        
    game_count += 1