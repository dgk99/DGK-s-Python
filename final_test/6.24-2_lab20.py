# 메뉴로 구성 된 구구단과 삼각형 출력 프로그램
# 이번엔 함수로 묶어 동작 시켜보기

# 구구단 함수
def make_dan():
    input_list = []
    for i in dan_input:
        if i == "~":
            del dan_input[i]
    input_list.append(int(i))
    print(input_list)
    # 구구단 반복문
    if len(input_list) == 1:
        for dan in range(input_list[0], input_list[0] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
    else:
        for dan in range(input_list[0], input_list[1] + 1):
            for num in range(2, 10):
                print(f"{dan} * {num} = {dan * num}")
            print()
# 랜덤값 삼각형 함수
def make_triangle():
    pass

# 요구사항:

while True:
    # 1. 사용자에게 메뉴를 출력하고 입력을 받아 해당 기능을 실행 후 다시 메뉴로 돌아오는 기능
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
        print("출력할 구구단을아래 형식으로 입력하세요 (예: 2, 2~5)")
        dan_input = input()
        make_dan()
    # • 입력 형태에 따라 한 단만 또는 지정된 범위의 구구단을 출력
    # • 입력 값이 2~9 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    elif menu_input == 2:
        pass
    # – 랜덤값 삼각형 출력
    # • 사용자로부터 삼각형의 높이(2~3줄)를 입력 받음
    # • 입력된 높이에 맞춰 0~9사이 중복 되지 않은 난수를 생성하여 삼각형 모양으로 출력
    # • 입력 값이 2~3 범위를 벗어날 경우 에러 메시지를 출력하고 재입력 요구
    elif menu_input == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 사이의 값을 입력하세요")
    # – 종료
    # • 프로그램을 종료