# 중복되지 않은 1~10 사이의 정수 3개
# in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# in을 써서 만드는 경우
# 3 7 4 : pc
# 2 3 4 : me
# result : 1 strike, 1 ball

# 문제를 해결하려면 자릿수가 중요하고, 그 숫자가 있나 없나가 중요
# 리스트로 숫자들을 관리하면 되겠다

import random

pc_list = list()

count = 0

while count < 3:
    rand_value = random.randint(1, 10)
    fount_duplicated_value = False
    
    for sub_count in range(count):
        # 중복 값이 있을 경우
        if rand_value == pc_list :
            fount_duplicated_value = True
            break
        
    if not fount_duplicated_value :
        pc_list.append(rand_value)
        count += 1
        
        
        
# for count in range(3):

#     while True:
#         # 랜덤 값 생성 : GR
#         rand_value = random.randint(1, 10)
        
        # 생성된 랜덤 값이 리스트 내 없을 경우 로직 종료
        # if rand_value not in pc_list :
        #     pc_list.append(rand_value)
        #     break

        # not in 연산자를 안 쓴다면?
        # 리스트 내 존재 여부 확인이 어렵다...
        

    
    # pc_list.append(rand_value)
    
print(pc_list)

# 랜덤값을 생성하면, 리스트 안에 숫자와 중복이 되는지 확인해야 한다.
# 1. 그러면 일단 랜덤 값을 생성하고
# 2. 생성된 랜덤 값이 리스트 내 존재하는지 확인
# 3-1. 중복이라면, 다른 숫자를 생성해서 중복 확인(1번으로 유턴)
# 3-2. 중복이 아니라면, 리스트에 추가 후 종료