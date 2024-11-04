dice_list = list(map(int, input().split(" ")))

max_num = 0

for num in range(3):
    if dice_list[num] > max_num:
        max_num = dice_list[num]

price = 0

if dice_list[0] == dice_list[1] == dice_list[2]:
    price += (10000 + (dice_list[0] * 1000))
elif dice_list[0] == dice_list[1] or dice_list[0] == dice_list[2]:
    price += (1000 + (dice_list[0] * 100))
elif dice_list[1] == dice_list[2]:
    price += (1000 + (dice_list[1] * 100))
else:
    price = max_num * 100

print(price)