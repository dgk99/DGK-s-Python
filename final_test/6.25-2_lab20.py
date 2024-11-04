# 메뉴로 구성된 구구단과 삼각형 출력 프로그램

# 구구단 함수
import random


def make_dan(arg_dan):
    if len(arg_dan) == 2:
        for dan in range(arg_dan[0], arg_dan[1] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
    else:
        for dan in range(arg_dan[0], arg_dan[0] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()

# 랜덤값 삼각형 함수
def make_triangle(arg_del_num):
    # 공백 카운트
    blank_count = 1
    # 숫자 인덱스 카운트
    num_index = 0
    # 숫자 반복 카운트
    num_count = 1
    
    # 0~9 중 랜덤한 난수
    random_num = [int(value) for value in range(0, 10)]
    for _ in range(arg_del_num):
        del random_num[random.randint(0, len(random_num) - 1)]
    
    if input_high == 2:
        for _ in range(input_high):
            for _ in range(blank_count):
                print(" ",end="")
                blank_count -= 1
            for _ in range(num_count):
                print(random_num[num_index],end="")
                num_index += 1
                num_count += 1
            print()
    else:
        blank_count = 2
        for _ in range(input_high):
            for _ in range(blank_count):
                print(" ",end="")
            blank_count -= 1
            for _ in range(num_count):
                print(random_num[num_index],end="")
                num_index += 1
            num_count += 1
            print()
        

# 요구사항:
while True:
    # 1. 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
    print("*" * 20)
    print(f"1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료")
    print("*" * 20)
    menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    
    # 3. 각 기능에 따른 추가 입력 요구와 에러 처리를 포함

    # • 기능 상세
    # – 구구단 출력
    if menu_input == 1:
    # • 사용자로부터 출력할 구구단의 범위를 입력 받음
        print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
        input_dan = input()
        input_dan = [int(value) for value in input_dan.split("~")]
        if len(input_dan) == 2:
            if input_dan[0] >= 10 or input_dan[0] <= 1 or input_dan[1] >= 10 or input_dan[1] <= 1:
                print("2~9 사이의 값으로 입력하세요")
            else:
                make_dan(input_dan)
        else:
            if input_dan[0] >= 10 or input_dan[0] <= 1:
                print("2~9 사이의 값으로 입력하세요")
            else:
                make_dan(input_dan)
    # • 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
    # • 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    # – 랜덤값 삼각형 출력
    elif menu_input == 2:
        print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
        input_high = int(input())
        if input_high == 2:
            make_triangle(7)
        elif input_high == 3:
            make_triangle(4)
        else:
            print("2 또는 3을 입력하세요")
    # • 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음
    # • 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
    # • 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    elif menu_input == 3:
        print("프로그램을 종료합니다.")
        break
    # – 종료
    # • 프로그램을 종료
    # 2. 입력이 1~3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
    else:
        print("1~3 사이의 값을 입력하세요")