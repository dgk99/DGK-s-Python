now_time = input("현재 시각을 입력하세요: ")
now_time_list = list(map(int, now_time.split(" ")))
oven_time = int(input("조리 시간을 입력하세요: "))

cooking_time = now_time_list[0]
cooking_minute = now_time_list[1]

take_time = cooking_minute + oven_time

if take_time <= 60:
    cooking_minute = take_time
else:

    if take_time % 60 == 0:
        cooking_time += take_time // 60
        cooking_minute = 0
    else:
        cooking_minute = take_time - 60
        cooking_time += 1


if cooking_time >= 24:
    cooking_time = 0

print(cooking_time, cooking_minute)