# 기말고사 대비 연습 문제
# 종료를 입력할 때 까지 계속 반복
import random
# 구구단
def mutliple(arg_dan1, arg_dan2 = None):
    if arg_dan2 == None:
        arg_dan2 = arg_dan1
    for arg_dan1 in range(arg_dan1, arg_dan2 + 1):
        for num in range(1, 10):
            print(f"{arg_dan1} * {num} = {arg_dan1 * num}")
        print()
    # else:
    #     for arg_dan1 in range(arg_dan1, arg_dan2 + 1):
    #         for num in range(1, 10):
    #             print(f"{arg_dan1} * {num} = {arg_dan1 * num}")
    #         print()
            

# 삼각형
def make_tri(arg_num):
    num_list = [int(value) for value in range(0, 10)]
    for _ in range(arg_num ):
        del num_list[random.randint(0, len(num_list) - 1)]
    blank_count = 2
    num_count = 1
    index_count = 0
    for _ in range(tri_input):
        for _ in range(blank_count):
            print(" ", end="")
        blank_count -= 1
        for _ in range(num_count):
            print(num_list[index_count], end="")
            index_count += 1
        print()
        num_count += 1

# 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행후 다시 메뉴로 돌아오는 기능
while True:
    print('-' * 20)
    print("1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료")
    print('-' * 20)
    # 입력이 1 ~ 3 범위 외의 값일 경우 에러 메시지를 출력하고 재입력을 요구
    menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    
    
    if menu_input == 1:
        while True:
            print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
            dan_input = input()
            dan_input = dan_input.split("~")
            dan_input[0] = int(dan_input[0])
            if len(dan_input) == 1:
                if 2 > dan_input[0] or dan_input[0] > 9 :
                    print("2~9 사이의 값으로 입력하세요")
                else:
                    mutliple(dan_input[0])
                    break
            elif len(dan_input) == 2:
                dan_input[1] = int(dan_input[1])
                if dan_input[0] < 2 or dan_input[0] > 9 or dan_input[1] < 2 or dan_input[1] > 9:
                    print("2~9 사이의 값으로 입력하세요")
                else:
                    mutliple(dan_input[0], dan_input[1])
                    break
                
    elif menu_input == 2:
        while True:
            print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
            tri_input = int(input())
            if tri_input == 2:
                make_tri(7)
                break
            elif tri_input == 3:
                make_tri(4)
                break

            print("2 또는 3을 입력하세요")
                #continue
    # 각 기능에 따른 추가 입력 요구와 에러 처리를 포함


    elif menu_input == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 사이의 값을 입력하세요")

# 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
# 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력을 요구




# 랜덤값 삼각형 출력
# 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음




# 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구

# 종료
# 프로그램을 종료