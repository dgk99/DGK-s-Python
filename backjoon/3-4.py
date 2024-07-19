total = int(input()) 
num = int(input())

price = 0

for i in range(num):
    price_num = list(map(int, input().split(" ")))
    total_price = price_num[0] * price_num[1]
    price += total_price

if total == price:
    print("Yes")
else:
    print("No")