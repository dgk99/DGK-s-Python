# 윤년 = 4의 배수이면서 100의 배수 or 400의 배수가 아닐 때
num = int(input())

if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print(1)
else:
    print(0)