# 자연수를 입력받아 별을 출력한다
star = int(input("N 입력: "))
# 1. 첫 번째 줄 부터 n번째 줄 까지 별의 개수를 1개씩 증가시킨다
# 2. n번째 줄 이후부터는 별의 개수를 감소시켜 마지막 줄에는 별 1개를 출력한다
for i in range(1, star):
    print("*" * i)
    

for i in range(star, 0, -1):
    print("*" * i)
    