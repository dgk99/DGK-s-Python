# 1~1000사이의 정수 중 3의 배수 합 구하기

# sum = 0

# for num in range(1, 1001) :
#     if num % 3 == 0 :
#         sum += num
# print(sum)

# while문을 사용하여 3의 배수의 합 구하기

sum = 0
# while은 반복의 횟수가 정해져 있지 않을 때 사용
flag = True
while flag : # flag가 False가 될 때 까지 실행
    for num in range(1, 1001) : # 1부터 1000까지의 수 생성
        if num % 3 == 0 : # 수가
            sum += num
        flag = False
    print(f"1~1000 사이 정수 중 3의 배수의 총 합은 : {sum}")