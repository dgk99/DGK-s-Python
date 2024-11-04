# 가위 바위 보 게임 확장 ver
import random


# pc가 출력할 랜덤한 값을 리스트로 만들기
pc_choice_list = ["가위", "바위", "보"]

# 게임은 3판 2선승으로 진행
# 유저 승리 카운트, 패배 카운트, 무승부 카운트
user_win_count = 0
user_lose_count = 0
user_draw_count = 0

# 가위, 바위, 보 중 하나를 입력하지 않거나, 2선승이 나올 때 까지 반복되어야 하기에 while을 써서 반복한다.
while True :
    # pc_choice_list에서 랜덤으로 하나의 값을 가져오는 코드
    pc_choice = random.choice(pc_choice_list)
    
# 사용자로부터 가위 바위 보 중 하나를 입력받는다
    userinput = input("가위, 바위, 보 중 하나를 입력하세요: ")
    # 만약 유저 입력값이 가위, 바위, 보 이외의 값을 입력하면 다시 입력하라고 출력
    if userinput != "가위" and userinput != "바위" and userinput != "보" :
        print("가위, 바위, 보 중에서 선택하세요.")
        print()
    else: # 제대로 된 값을 입력했다면 컴퓨터의 랜덤 값 출력
        print(f"컴퓨터: {pc_choice}")
     

    # 유저입력값과 pc랜덤값이 같을 경우, 무승부를 출력하고 user_draw_count에 +1
    if (userinput == "가위" and pc_choice == "가위") or (userinput == "바위" and pc_choice == "바위") or (userinput == "보" and pc_choice == "보") :
        user_draw_count += 1
        print(f"무승부! 현재 전적: {user_win_count}승 {user_lose_count}패 {user_draw_count}무\n")
        
        
    # 유저입력값이 pc랜덤값을 이길 경우, 승리를 출력하고 user_win_count에 +1
    elif (userinput == "가위" and pc_choice == "보") or (userinput == "바위" and pc_choice == "가위") or (userinput == "보" and pc_choice == "바위") :
        user_win_count += 1
        print(f"승리! 현재 전적: {user_win_count}승 {user_lose_count}패 {user_draw_count}무\n")
        
        
    # 유저입력값이 pc랜덤값에 질 경우, 패배를 출력하고 user_lose_count에 +1
    elif (userinput == "가위" and pc_choice == "바위") or (userinput == "바위" and pc_choice == "보") or (userinput == "보" and pc_choice == "가위") :
        user_lose_count += 1
        print(f"패배ㅠㅠ 현재 전적: {user_win_count}승 {user_lose_count}패 {user_draw_count}무\n")
        

# 게임이 종료되면 전체 승 패 무의 결과와 최종 승자 출력
    if user_win_count == 2 or user_lose_count == 2 :
        break

# 경기 수 카운트가 3이 되거나, 승리 카운트가 유저나 컴퓨터가 2가 되면 프로그램 종료 후
# 지금까지의 결과 기록을 모두 출력하고 승자도 출력
print(f"전적: {user_win_count}승 {user_lose_count}패 {user_draw_count}무")
if user_win_count == 2 :
    print("최종 승자: 사용자")
else:
    print("최종 승자: PC")
    
    
# in, not in 연산자 사용금지

