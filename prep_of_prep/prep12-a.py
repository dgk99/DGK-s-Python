# 가위 바위 보 게임 만들기

# 컴퓨터가 난수를 이용해 가위 바위 보 중 하나를 무작위로 선택하게 하세요
# 이기면 승리, 지면 패배, 비기면 무승부를 출력하시오

import random

user = input("가위, 바위, 보 중 하나를 선택하세요: ")

choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)

print(f"컴퓨터의 선택: {computer_choice}")

if user == "가위" and computer_choice == "보" or user == "바위" and computer_choice == "가위" or user == "보" and computer_choice == "바위" :
    print("결과: 당신이 이겼습니다!")
    
elif user == "가위" and computer_choice == "가위" or user == "바위" and computer_choice == "바위" or user == "보" and computer_choice == "보" :
    print("결과: 무승부입니다!")
    
elif user == "가위" and computer_choice == "바위" or user == "바위" and computer_choice == "보" or user == "보" and computer_choice == "가위" :
    print("결과: 당신이 졌습니다!")
    
elif user != "가위" or user != "바위" or user != "보" :
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요") 