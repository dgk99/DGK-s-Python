# 기말고사 1번 문제 풀이

import random

trial_count = 1000

dice_list = [0, 0, 0, 0, 0, 0]

# trial_count만큼 랜덤 숫자를 발생 : 1 ~ 6
for _ in range(trial_count):
    # 생성된 랜덤 값에 따른, 각 주사위 번호의 횟수를 증가
    rand_num = random.randint(1, 6)
    
    dice_list[rand_num - 1] += 1
    
max_event = -1
for index in range(6):
    if dice_list[index] > max_event:
        max_event = dice_list[index]
# 히스토그램과 확률을 계산
# 주사위 1이 나올 확률 : (E1 / trial_count) x 100
for index in range(7):
    print(int(dice_list[index] / max_event) * 10)
    print(f"{index + 1}번 확률: {(dice_list[index + 1] / trial_count) * 100}")