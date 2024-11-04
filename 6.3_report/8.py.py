# 숫자 맞추기 게임
import random
# while문과 break문을 사용하여 1부터 100사이의 숫자를맞추는 게임 작성
# 사용자가 숫자를 맞출 때 까지 반복하고, 맞추면 반복을 종료
# 정답 숫자는 랜덤 함수를 이용하여 1에서 100사이의 임의 정수 선택

# 먼저 컴퓨터가 1부터 100까지 숫자 생성하고 리스트에 저장
num_list = []
for num in range(1, 101) :
    num_list.append(num)

# 1부터 100이 있는 리스트에서 랜덤으로 숫자 하나 빼오기
random_num = random.choice(num_list)


while True :
    inputValue = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    
    if inputValue == random_num :
        print("정답입니다!")
        break
    elif inputValue < random_num :
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")
    

