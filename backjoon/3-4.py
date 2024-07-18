total = int(input("총 금액: ")) 
num = int(input("물건 종류 수: "))

price = 0

for i in range(num):
    price_num = input(f"물건의 가격과 갯수 입력({i + 1}번째): ")
    price_num = list(map(int, price_num.split(" ")))
    total_price = price_num[0] * price_num[1]
    price += total_price

if total == price:
    print("Yes")
else:
    print("No")