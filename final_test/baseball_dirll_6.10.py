# 야구 게임

# 컴퓨터 난수 생성
# 생성된 난수를 저장할 리스트
import random
com_list = []
# 리스트에 저장된 갯수를 확인할 카운트
count = 0
# 리스트에 중복되지 않은 수가 3개가 들어갈 때 까지 반복해야 하니까 while문에 조건문을 넣어 생성
while count < 3:
    # 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성
    random_num = random.randint(0, 9)
    # count수만큼 반복하는 코드 작성. 초기에는 count값이 0이니까, 반복하지 않아 바로 else로 이동
    for index in range(count):
        if com_list[index] == random_num:
            break
    else:
        com_list.append(random_num)
        count += 1
print(com_list)

# 게임 시도 횟수, 아웃 count 생성
game_count = 1
o = 0

while True:
    # 플레이어 입력
    # 유저가 입력한 값을 저장할 리스트 생성
    user_list = []
    # 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
    for _ in range(3):
        user_input = int(input("정수를 입력하세요: "))
        user_list.append(user_input)
    
    # 볼, 스트라이크 count 생성
    b, s = 0, 0
    
    # 현재 상황 중계
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_list[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
                    
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")
    
    
    if s == 0 and b == 0:
        o += 1
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    else:
        print(f"결과: {s} Strike, {b} Ball")
        
    # 게임 패배 조건
    # 시도 횟수가 5번 이상
    if game_count == 5:
        print("게임 종료: 패배 (시도 횟수 5회 초과)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    # 스트라이크 아웃 횟수가 2회 이상
    elif o == 2:
        print("게임 종료: 패배 (스트라이크 아웃 2회 이상)")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    
    

    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    if s == 3:
        print("게임 종료: 승리")
        print(f"정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    
    game_count += 1
