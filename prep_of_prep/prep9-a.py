# 평균 속도 계산기

# 차량이 어떤 거리를 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도를 계산하시오
# 사용자로부터 출발 시간과 도착 시간(시와 분으로 별도 입력), 그리고 이동거리를 받으시오
# 이 정보를 사용해 차량의 평균 속도를 km/h 단위로 계산하고,
# 그 속도가 "느림", "보통", "빠름" 중 어느것인지 고르시오

#출발 시간 start time = st
st = int(input("출발 시 (시간)을 입력하세요: "))
#출발 분 start minute = sm
sm = int(input("출발 시 (분)을 입력하세요: "))
#도착 시간 arrived time = at
at = int(input("도착 시 (시간)을 입력하세요: "))
#도착 분 arrived minute = am
am = int(input("도착 시 (분)을 입력하세요: "))
#이동 거리 travel distance = td
td = int(input("이동 거리(km)를 입력하세요: "))

def speed():
    totaltime = (((at - st) * 60) + (am - sm)) / 60
    averagespeed = td / totaltime
    
    print(f"이동 거리: {float(td)}km")
    print(f"출발 시간: {st}시 {sm}분")
    print(f"도착 시간: {at}시 {am}분")
    print(f"평균 속도: {averagespeed:.2f}km/h")
    
    if averagespeed < 60 :
        averagespeed = "느림"
    elif 60 <= averagespeed < 90 :
        averagespeed = "보통"
    else:
        averagespeed = "빠름"
        
    print(f"속도 상태: {averagespeed}")
    
speed()

