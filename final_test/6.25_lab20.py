import random


def make_dan(arg_dan, arg_dan2 = None):
    if arg_dan2 == None:
        arg_dan2 = arg_dan + 1
        for dan in range(arg_dan, arg_dan2):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
    else:
        for dan in range(arg_dan, arg_dan2 + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
            
def make_triangle(arg_del_num):
    # 0~9 정수 리스트
    num_list = [int(value) for value in range(0, 10)]
    for _ in range(arg_del_num):
        del num_list[random.randint(0, len(num_list) - 1)]
    # 공백, 숫자 삼각형 반복문
    blank_count = 1
    num_count = 1
    if input_high == 3:
        blank_count = 2
        num_count = 1
    num_list_count = 0
    for _ in range(input_high):
        for _ in range(blank_count):
            print(" ",end="")
        blank_count -= 1
        for _ in range(num_count):
            print(num_list[num_list_count],end="")
            num_list_count += 1
        num_count += 1
        print()

# 요구사항:
    # 1. 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
while True:
    print("*" * 20)
    print("1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료")
    print("*" * 20)
    menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    # 2. 입력이 1~3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
    if 1 > menu_input or menu_input > 3:
        print("1~3 사이의 값을 입력하세요")
    # 3. 각 기능에 따른 추가 입력 요구와 에러 처리를 포함
    # • 기능 상세
    # – 구구단 출력
    if menu_input == 1:
        # • 사용자로부터 출력할 구구단의 범위를 입력 받음
        print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
        input_dan = input()
        input_dan = [int(input_dan) for input_dan in input_dan.split("~")]
        # • 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
        if len(input_dan) == 2:
            if input_dan[0] > 9 or input_dan[0] < 1 or input_dan[1] > 9 or input_dan[1] < 1:
                # • 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
                print("2~9 사이의 값을 입력하세요")
            else:
                make_dan(input_dan[0], input_dan[1])
        else:
            if input_dan[0] > 9 or input_dan[0] <= 1:
                print("2~9 사이의 값을 입력하세요")
            else:
                make_dan(input_dan[0])

    # – 랜덤값 삼각형 출력
    elif menu_input == 2:
    # • 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음
        print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
        input_high = int(input())
        if input_high == 2 :
            make_triangle(7)
        elif input_high == 3:
            make_triangle(4)
        else:
            # • 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
            print("2 또는 3을 입력하세요")
            
        
    # • 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
    
    elif menu_input == 3:
        print("프로그램을 종료합니다.")
        break
    
    # – 종료
    # • 프로그램을 종료
    else:
        print("1~3 사이의 값을 입력하세요")