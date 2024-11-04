# 숫자 맞추기 게임 확장 버전

# 컴퓨터가 1부터 100사이의 숫자를 랜덤하게 선택
# 사용자는 숫자를 맞추기 위해 시도함. 사용자에게 10번의 기회가 주어짐
# 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "더 큰 숫자입니다."라고 출력
# 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "더 작은 숫자입니다."라고 출력
# 사용자가 숫자를 맞추면 "정답입니다!"라고 출력되고 게임 종료
# 10번의 시도가 끝날 때 까지 숫자를 맞추지 못하면 "모든 기회를 사용하였습니다. 정답은 [숫자]입니다."라고 출력
# 사용자가 0을 입력하면 언제든지 게임이 종료됨.

import random
# 먼저 컴퓨터가 1부터 100까지 숫자 생성하고 리스트에 저장
num_list = []
for num in range(1, 101) :
    num_list.append(num)

# 1부터 100이 있는 리스트에서 랜덤으로 숫자 하나 빼오기
random_num = random.choice(num_list)

# 사용자의 기회 카운트
user_count = 0

while True :
    inputValue = int(input(f"기회{user_count}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))
    
    if inputValue == 0 :
        break
    
    if user_count == 10 and inputValue == random_num :
        print("정답입니다!")
        break
    
    elif user_count == 10 :
        print(f"모든 기회를 사용하였습니다. 정답은 {random_num}입니다")
        break
    
    elif inputValue == random_num :
        print("정답입니다!")
        break
    elif inputValue < random_num :
        print("더 큰 숫자입니다.")
        user_count += 1
    elif inputValue > random_num:
        print("더 작은 숫자입니다.")
        user_count += 1
    
print("게임이 끝났습니다.")