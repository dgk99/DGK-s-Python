# 나머지

#(a + b)%c == ((a % c) + (b % c))%c) ?
#(a * b)%c == ((a % c) * (b % c))%c) ?

# 세 수가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램 작성

a = int(input())
b = int(input())
c = int(input())

first = (a+b)%c
second = ((a+b) + (b%c))%c
third = (a*b)%c
forth = ((a%c) * (b%c))%c

print(first)
print(second)
print(third)
print(forth)