time = input("설정하고 싶은 알람 시간을 입력하세요: ")
time = list(map(int, time.split(" ")))
if time[0] == 0:
    time[0] = 24
late_45m_time = time[0] - 1, time[1] + 15
print(late_45m_time[0], late_45m_time[1])