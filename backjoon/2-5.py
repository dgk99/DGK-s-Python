time = list(map(int, input().split(" ")))
if time[0] == 0:
    time[0] = 24
print(time[0] - 1, time[1] + 15)