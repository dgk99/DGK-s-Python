time, minute = map(int, input().split(" "))
oven_time = int(input())

if minute + oven_time <= 60:
    minute += oven_time
else:
    if (minute + oven_time) % 60 == 0:
        time += ((minute + oven_time) // 60)
        minute = 0
    else:
        minute += oven_time - 60
        time += 1

if time >= 24:
    time -= 24

print(time, minute)