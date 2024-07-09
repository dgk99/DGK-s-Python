# • 문제 설명
# – 사용자로부터 Start, End, N의 세 값을 입력 받는다
# – 이 값들을 사용하여 Start와 End 사이에서 중복되지 않은 N개의 난수를 생성 후 1차원 리스트에 저장
# 후 출력하는 프로그램을 작성하세요

import random


while True:
    print("난수를 생성할 범위와 개수를 입력하세요.")
# • 입력
    while True:   
    # – Start: 난수의 시작 범위
        num_start = int(input("Start (0 이상의 정수): "))
        # • 0 이상, End보다 작아야 함
        if num_start <= 0:
            print("Start는 0보다 커야 합니다.")
        else:
            break

    while True:
        # – End: 난수의 끝 범위
        num_end = int(input("End (Start보다 큰 정수): "))
        # • Start보다 커야 함
        if num_end < num_start:
            print(f"End는 Start({num_start})보다 커야 합니다.")
        else:
            break
        
    while True:
        # – N: 생성할 난수의 수
        num_n = int(input("N (생성할 난수의 개수): "))
        # • Start와 End 사이 가능한 최대 수 이하
        if num_n < num_start or num_n > num_end:
            print(f"N은 {num_start}부터 {num_end} 사이의 정수여야 합니다.")
        else:
            break
    while True:
        random_list = []
        count = 0
        random_num = random.randint(num_start, num_end)
        for _ in range(count):
            
            if random_list[count] == random_num:
                break
        else:
            random_list.append(random_num)
            count += 1
        
print(random_list)
# • 요구사항
# 1. 모든 입력 값은 유효할 때까지 재입력을 요구한다
# 2. Start는 0 이상이며 End보다 작아야 한다
# 3. End는 Start보다 커야 한다
# 4. N은 Start와 End 사이의 정수 범위 내에서 입력되어야 한다
# 5. 생성된 난수 값은 1차원 리스트에 저장 되어야 한다
# • 출력
# – 생성된 중복되지 않은 N개의 난수를 포함한 리스트를 출력한다