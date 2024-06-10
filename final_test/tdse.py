# 야구 문제
import random
# 컴퓨터 난수 생성
# 0부터 9까지의 난수를 3개 생성
# 난수를 저장할 리스트 만들기
com_list = []
# 리스트에 들어갈 숫자 카운트
count = 0
# 중복되지 않는 숫자가 나올 때 까지 반복해야 하니 while문 사용
while count < 3: # 리스트에 숫자 3개가 들어가면 반복문을 종료하는 조건문
    # 0부터 9까지의 난수 생성하는 코드
    random_num = random.randint(0, 9)
    for i in range(count):
        if com_list[i] == random_num:
            break
    else:
        com_list.append(random_num)
        count += 1

# 게임 카운트, 아웃 카운트 생성
game_count = 1 # 시도 횟수가 1부터 시작하니 게임 카운트도 1부터
out = 0 # while문 안에 있으면 아웃값이 초기화 되지 않아 아웃으로 인한 종료가 불가능 하기에 while문 밖에 둠
# 플레이어 입력

while True:
    user_list = []
    # 키보드를 통해 0부터 9까지의 수 입력
    for _ in range(3):
        user_input = int(input("0부터 9까지의 정수를 입력하세요: "))
        user_list.append(user_input)
    
    # 스트라이크, 볼 카운트
    s, b = 0, 0
    
    # 현재 상황 중계
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_list[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
                    
    print(com_list)
    
    # 시도, 입력한 숫자 출력
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")
    game_count += 1
    # 결과 출력 중계
    if s == 0 and b == 0:
        out += 1
        print(f"결과: {s} Strike, {b} Ball, {out} Out")
    else:
        print(f"결과: {s} Strike, {b} Ball")
    
    # 게임 패배 조건
    # 시도 횟수가 5회 이상
    if game_count > 5:
        print("게임 종료: 패배 (시도 횟수 5회 초과)")
        break
    # 스트라이크 아웃 횟수가 2회 이상
    elif out >= 2:
        print("게임 종료: 패배 (스트라이크 아웃 2회 이상)")
        break

    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    elif s == 3:
        print("게임 종료: 승리")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break