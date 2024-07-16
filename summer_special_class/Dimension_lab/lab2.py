# • 문제 설명
# – 사용자로부터 행과 열의 수를 입력 받아, 해당 크기에 맞는 2차원 리스트를 생성
# – 사용자는 각 요소에 들어갈 값을 직접 입력하고,
# – 입력이 완료되면 완성된 2차원 리스트를 출력

# • 프로그램 실행 절차
# – 행과 열의 수 입력 받기
# • 사용자에게 2차원 리스트의 행(rows)과 열(cols)의 수를 입력 받는다
# 행 입력
num_row = int(input("Enter the number of rows: "))
# 열 입력
num_col = int(input("Enter the number of columns: "))

# – 2차원 리스트 생성
# • 입력 받은 행과 열의 수에 따라 초기화된 2차원 리스트를 생성한다
num_list = []
# – 리스트 값 입력
# • 사용자로부터 각 위치의 요소에 들어갈 값을 입력 받아 리스트에 저장
for row in range(num_row):
    for col in range(num_col):
        input_num = int(input(f"Enter value for [{row}][{col}]: "))
        num_list.append(input_num)
# – 리스트 출력
# • 완성된 리스트를 출력하여 사용자가 입력한 모든 값이 올바르게 저장되었는지 확인
count = 0
for i in num_list:
    print(i, end=" ")
    count += 1
    if count % 3 == 0:
        print("")