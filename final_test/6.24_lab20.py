# 메뉴로 구성 된 구구단과 삼각형 출력 프로그램

# 기능 상세
# 구구단 출력
import random

def make_dan():
    # 사용자로부터 출력할 구구단의 범위를 입력 받음
    # 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 입력
    if len(input_dan) == 2:
        for dan in range(input_dan[0], input_dan[1] + 1):
            for num in range(2, 9):
                print(f"{dan} * {num} = {dan * num}")
            print()
    else:
        for dan in range(input_dan[0], input_dan[0] + 1):
            for num in range(2, 9):
                print(f"{dan} * {num} = {dan * num}")
            print()
    # 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    
# 랜덤값 삼각형 출력
def make_triangle():
    # 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음
    # 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
    # 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    # 0~9까지의 정수 리스트
    num_list = [int(value) for value in range(0, 10)]
    if input_high == 2:
        for _ in range(7):
            del num_list[random.randint(0, len(num_list) - 1)]
    else:
        for _ in range(4):
            del num_list[random.randint(0, len(num_list) - 1)]
    # 공백, 삼각형 생성 반복문
    b_count = 2
    n_count = 1
    r_n_count = 0
    for _ in range(input_high):
        for _ in range(b_count):
            print(" ",end="")
        b_count -= 1
        for _ in range(n_count):
            print(num_list[r_n_count],end="")
            r_n_count += 1
        n_count += 1
        print()
            

# 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
while True:
    print("*" * 20)
    print("1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료")
    print("*" * 20)
    menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    # 입력이 1~3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
    if 1 <= menu_input <= 3:
        if menu_input == 1:
            print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
            input_dan = input()
            input_dan = input_dan.split("~")
            input_dan[0] = int(input_dan[0])
            if len(input_dan) == 2:
                input_dan[1] = int(input_dan[1])
                if input_dan[0] < 2 or input_dan[0] > 9 or input_dan[1] < 2 or input_dan[1] > 9:
                    print("2~9 사이의 값으로 입력하세요")
                else:
                    make_dan()
            elif len(input_dan) == 1:
                if input_dan[0] < 2 or input_dan[0] > 9:
                    print("2~9 사이의 값으로 입력하세요")
                else:
                    make_dan()
        elif menu_input == 2:
            print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
            input_high = int(input())
            if input_high == 2 or input_high == 3:
                make_triangle()
            else:
                print("2 또는 3을 입력하세요")
        else:
            print("프로그램을 종료합니다.")
            break
    else:
        print("1~3 사이의 값을 입력하세요")
  
    # 각 기능에 따른 추가 입력 요구와 에러 처리를 포함





# 종료
# 프로그램을 종료