# 가위바위보 게임 만들기

# 사용자 입력은 input()으로 받기
userinput = input("가위, 바위, 보 중 하나를 선택하세요: ")
# 컴퓨터의 선택은 난수 발생을 이용해 결정하세요. random 모듈의 choice() 함수 사용


# 랜덤 가위바위보 코드
import random

choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)

print("컴퓨터의 선택 :",computer_choice)

# 사용자가 잘못된 값을 입력했을 경우
if userinput != '가위' and userinput != '바위' and userinput != '보' :
    print("잘못된 입력입니다. 가위, 바위 보 중에서 선택해주세요")
    
# 사용자가 무승부 일 경우
if computer_choice == '가위' and userinput == '가위':
    print("결과: 무승부입니다!")
elif computer_choice == '바위' and userinput == '바위' :
    print("결과: 무승부입니다!")
elif computer_choice == '보' and userinput == '보' :
    print("결과: 무승부입니다!")
   
# 사용자가 질 경우 
if computer_choice == '가위' and userinput == '보' :
    print("결과: 당신이 졌습니다!")
elif computer_choice == '보' and userinput == '바위' :
    print("결과: 당신이 졌습니다!")
elif computer_choice == '바위' and userinput == '가위' :
    print("결과: 당신이 졌습니다!")

# 사용자가 이길 경우
if computer_choice == '가위' and userinput == '바위' :
    print("결과: 당신이 이겼습니다!")
elif computer_choice == '보' and userinput == '가위' :
    print("결과: 당신이 이겼습니다!")
elif computer_choice == '바위' and userinput == '보' :
    print("결과: 당신이 이겼습니다!")