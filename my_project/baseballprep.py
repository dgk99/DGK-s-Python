# 야구 문제

import random

# 사용자에게 시도횟수 출력해주면서 값 3개 받기
user_input = print("0 ~ 9 사이의 정수를 입력하시오")
user_input1 = int(input())
user_input2 = int(input())
user_input3 = int(input())

# 유저가 입력한 값을 리스트에 저장
user_input_list = []
user_input_list.append(user_input1)
user_input_list.append(user_input2)
user_input_list.append(user_input3)

count_cpu = 0
list_cpu = []
# 컴퓨터가 총 랜덤 값 3개를 내야 한다.

# 컴퓨터가 1번째 랜덤 값을 낸다
for i in range(3) :
    random_cpu = random.randint(0, 9)
    list_cpu.append(random_cpu)
    count_cpu += 1
    


# 리스트에 저장
# 두 번째 값 부터는 리스트에 있는 수랑 비교
# 중복이면 다시 랜덤 값 생성.
# 아니면 리스트에 저장
# 이걸 3번 반복 후 탈출

# 근데,3개가 중복되지 않게 하기

# 중복이 나오지 않을 때 까지 반복하기

# 사용자 값과 컴퓨터 값을 비교하고, strike or ball 탐지하기

# 총 게임 횟수가 5회거나, 스트라이크 아웃이 2회면 게임 종료

# 스트라이크가 3개 이상이면 승리