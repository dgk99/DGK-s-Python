# 메뉴로 구성된 구구단, 삼각형 출력

# 구구단 함수
def make_dan(arg_dan):
    arg_dan[0] = int(arg_dan[0])
    if len(arg_dan) == 1:
        for dan in range(arg_dan[0], arg_dan[0] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
    else:
        arg_dan[1] = int(arg_dan[1])
        for dan in range(arg_dan[0], arg_dan[1] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
            
# • 요구사항:
# 1. 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
while True:
    print("*" * 20)
    print(f"1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료")
    print("*" * 20)
    menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    

    # • 기능 상세
    # – 구구단 출력
    if menu_input == 1:
        print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
        input_dan = input()
        input_dan = input_dan.split("~")
        for i in input_dan:
            i = int(i)
        input_dan.append(i)
        print(type(input_dan[0]))
        # make_dan(input_dan)
    # • 사용자로부터 출력할 구구단의 범위를 입력 받음
    # • 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력

    # • 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    
    # – 랜덤값 삼각형 출력
    elif menu_input == 2:
        pass
    # • 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음
    # • 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
    # • 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    

    # – 종료
    elif menu_input == 3:
    # • 프로그램을 종료
        print("프로그램을 종료합니다.")
        break
    
    # 2. 입력이 1~3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
    # 3. 각 기능에 따른 추가 입력 요구와 에러 처리를 포함
    else:
        print("1~3 사이의 값을 입력하세요")