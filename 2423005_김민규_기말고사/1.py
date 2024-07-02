# 구현 내용
# 1. 사용자 입력



import random

while True:
    # 사용자로부터 주사위를 던질 횟수 N을 입력받는다
    n = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
    # 입력 범위는 100에서 1000000 사이이다
    # 유효하지 않은 값을 입력할 경우, 재입력을 요청한다
    if n < 100 or n > 1000000:
        print("Please enter a numver within the specified range.")
    else:
        
        # 1~6까지의 숫자 카운트
        num_1 = 0
        num_2 = 0
        num_3 = 0
        num_4 = 0
        num_5 = 0
        num_6 = 0
        
        # 난수 생성 및 카운트
        # 사용자가 입력한 횟수 N만큼 주사위를 던진다
        for i in range(n):
            random_num = random.randint(1, 6)
            if random_num == 1:
                num_1 += 1
            elif random_num == 2:
                num_2 += 1
            elif random_num == 3:
                num_3 += 1
            elif random_num == 4:
                num_4 += 1
            elif random_num == 5:
                num_5 += 1
            else:
                num_6 += 1
        print(num_1, num_2, num_3, num_4, num_5, num_6)
        break
    # 주사위의 결과는 1부터 6 사이의 숫자이다
    # 각 숫자의 발생 횟수를 카운트한다
num_list = [num_1, num_2, num_3, num_4, num_5, num_6]
# 결과 시각화
# 1부터 6까지 각 숫자의 발생 빈도를 히스토그램으로 시각화한다

# 가장 큰 숫자를 찾는 조건문
max_num = 0
for i in num_list:
    if i > max_num:
        max_num = i

print("Dice Roll Frequency Histogram:")

# num_list의 index list
index = 0       
# 출력할 때 사용할 숫자 카운트
printed_num = 1
# 별 생성하는 조건문
for j in range(6):
    if  num_list[j] == max_num :
        star = "*" * 10
        print(f"{printed_num}: {star} ({num_list[index]} times, {num_list[index] / n}%)")

    else:
        star_count = (num_list[j] / max_num) * 10
        print(f"{printed_num}: {int(star_count) * "*"} ({num_list[index]} times, {num_list[index] / n}%)")
    printed_num += 1
    index += 1
# 히스토그램에서 각 *는 발생 빈도의 최대치에 대한 상대적인 비율로 나타내며, 최대 10개의 *를 표시한다



# 각 숫자별로 발생 횟수와 확률을 표시한다
# 확률은 발생 횟수 / 총 시도 횟수로 계산된다