# 사용자로부터 거리를 km단위로 입력받습니다.
distance = int(input("여행할 거리를 킬로미터(km) 단위로 입력하세요: "))

# 빛의 속도는 초당 299,792km입니다.
speed = 299792

# 시간 = 거리/속도
time = distance / speed

#빛이 해당 거리를 여행하는데 걸리는 시간을 계산하여 화면에 출력합니다.
print("빛이", float(distance),"킬로미터를 여행하는 데 걸리는 시간은", time , "초입니다.")