# 1에서 100까지의 범위 내에서 중복되지 않는 랜덤 정수를 생성하고, 이를 리스트에 저장한 후 사용자가
# 입력한 인덱스에 해당하는 값을 출력합니다.

# 사용자는 먼저 생성할 랜덤 정수의 개수 N을 입력합니다. N은 1 이상 100 이하의 정수여야 합니다. 
n = int(input("N값을 입력하세요 (1-100): "))
random_list = []
if n < 0 or n > 101 :
    print("에러: N은 1 이상 100 이하의 정수여야 합니다.")
else: # 입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성합니다.
    import random
    for _ in range(0, n) :
        random_number = random.randint(1, 100)
        random_list.append(random_number)
# 생성된 랜덤 숫자들은 리스트에 저장됩니다.
print("생성된 리스트: ",random_list)
# 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받습니다. 인덱스는 0부터 N−1까지의 값이어야 합니다. 
index_number = int(input(f"원하는 원소의 인덱스 범위를 입력하세요 (0-{n-1}): "))
if index_number > n or index_number < 0 :
    print("에러: 유효한 인덱스 범위를 벗어났습니다.")
else:
    print("선택한 인덱스 원소: ",random_list[index_number])
# 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.