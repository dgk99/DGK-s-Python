# 야구 게임 만들기

# 컴퓨터가 3개의 난수를 생성하고 플레이어가 맞추는 게임.
import random
com_list = []
count = 0
# 1. 컴퓨터 난수 생성
# 3개의 정수를 랜덤으로 생성하는데, 중복값이 안나올 때 까지 생성해야 하니 while 사용
while count < 3:
    # 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성
    random_num = random.randint(0, 2)
    # 생성된 난수가 중복되면 안됌!
    for i in range(count):
        if random_num == com_list[i]:
            break
    else:
        com_list.append(random_num)
        count += 1

# 2. 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력
# 예외 처리는 하지 않음. 올바른 입력이 들어온다고 가정 

game_count = 1
out = 0

while True:
    user_num = [int(num) for num in input(f"[{game_count}번째 시도] 세자리 숫자 입력: ")]
    # 스트라이크, 볼 카운터
    s, b = 0, 0
    # 랜덤값과 유저값 비교, 결과 출력
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_num[j]:
                if i == j:
                    s += 1
                else:
                    j += 1

    if s == 0 and b == 0:
        out += 1
        print(f"입력한 숫자 - {user_num[0]} {user_num[1]} {user_num[2]}")
        print(f"결과: Out!")
    else:
        print(f"입력한 숫자 - {user_num[0]} {user_num[1]} {user_num[2]}")
        print(f"결과: {s} Strike, {b} Ball, {out} Out")
        
    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    if s == 3:
        print("게임 종료: 승리")
        break
    # 3. 게임 패배 조건
    # 시도 횟수가 5번 이상일 경우
    # 스트라이크 아웃 횟수가 2번 이상일 경우
    elif out == 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 이상)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    elif game_count == 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 이상)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    else:
        game_count += 1





