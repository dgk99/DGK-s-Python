import random
com_list = [] # 컴퓨터의 3자리 숫자
count = 0
# 리스트 내 중복 검사
while count < 3:
    randon_num = random.randint(0, 9) # 0부터 9까지 랜덤으로 호출
    for i in range(count): # 카운트만큼 돌건데 (맨 처음 호출된 숫자는 카운트가 0이라 바로 else로 이동)
        if randon_num == com_list[i]: # 리스트내 i번째랑 인덱스랑 비교해서 돌아감
            break
    else:
        com_list.append(randon_num) # 리스트에 랜덤호출된 숫자 추가
        count += 1

game_count = 1 # 게임 카운트 정의
out = 0 # 스트라이크 아웃 정의

while True:
    # 세자리 수를 입력받고 리스트에 저장
    user_num = [int(num) for num in input(f"[{game_count}번째 시도] 세자리 숫자 입력: ")] 
    # 스트라이크, 볼 정의
    s, b = 0, 0
    # for문을 사용하여 user리스트와 com리스트를 비교
    for i in range(3):
        for j in range(3):
            if com_list[i] == user_num[j]: # com_list의 i번째 인덱스랑 user_num의 j번째 인덱스가 같을때 
                if i == j: # 인덱스 값이 자리랑도 같으면 스트라이크 
                    s += 1
                else: # 값만 같고 자리가 다르면 볼
                    b += 1
                break
    
    # 현재상황 분석
    if s == 0 and b == 0: # 스트라이크도 볼도 안나오면 아웃
        out += 1
        print(f"입력한 숫자 - {user_num[0]} {user_num[1]} {user_num[2]}\n결과: Out!\n")
    else: # 뭐든 하나라도 있으면 상황 출력
        print(f"입력한 숫자 - {user_num[0]} {user_num[1]} {user_num[2]}\n결과: {s} Strike, {b} Ball, {out} Out\n")
    
    # 게임 결과 출력
    if s == 3:
        print(f"게임 종료: 승리")
        break
    elif out == 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 이상)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    elif game_count == 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 초과)\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break
    else:
        game_count += 1