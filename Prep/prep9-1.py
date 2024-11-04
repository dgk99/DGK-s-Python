#차량이 어떤 거리를 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도를 계산하는 프로그램
#사용자로부터 출발시간과 도착시간(시와 분으로 별도 입력)그리고 이동거리를 입력받습니다.
#이 정보를 사용해 차량의 평균 속도를 km/h단위로 계산하고, 그 속도가 "느림", "보통", 또는 "빠름" 중 어느 것에 해당하는지 출력하세요.
# 출발 시간(start_time = st) 입력받기
st = int(input("출발 시 (시간)을 입력하세요: "))
# 출발 분(start_minute = sm) 입력받기
sm = int(input("출발 시 (분)을 입력하세요: "))
# 도착 시간(arrival_time = at) 입력받기
at = int(input("도착 시 (시간)을 입력하세요: "))
# 도착 분(arrival_minute = am) 입력받기
am = int(input("도착 시 (분)을 입력하세요: "))
# 이동 거리(travel_distance = td) 입력받기
td = int(input("이동 거리(km)를 입력하세요: "))

# 평균 속도(average_speed = avs) = 이동 거리(km)(td) / 총 이동 시간(h)(tatal_hour = th)
avs = td / ((((at - st)*60) + (am - sm))/60)

# 총 이동 시간(h) 계산식
# (((at - st)*60) + (am - sm))

# 이동 거리를 출력하자
print("이동 거리: ",float(td),"km")
# 출발 시간을 출력하자
print("출발 시간: ",st,"시", sm,"분")
# 도착 시간을 출력하자
print("도착 시간: ",at,"시", am,"분")
# 평균 속도를 출력하자
print("평균 속도: ",float(avs),"km/h")
# 평균 속도가 60km/h 미만이면, "느림" 출력
if avs < 60 :
    print("속도 상태: 느림")
# 평균 속도가 60km/h 이상, 90km/h미만이면, "보통" 출력
elif 60 <= avs < 90 :
    print("속도 상태: 보통")
# 평균 속도가 90km/h 이상이면, "빠름" 출력
elif avs >= 90 :
    print("속도 상태: 빠름")
#print(avs,"km/h")
