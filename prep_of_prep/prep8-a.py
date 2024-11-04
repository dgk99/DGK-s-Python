# 온도에 따른 활동 추천 프로그램

# 사용자로부터 현재 온도(섭씨)를 받습니다.
outdoor = int(input("현재 온도(섭씨)를 입력하세요: "))
# 입력받은 온도에 따라, 적합한 야외 활동을 추천하세요
# 30도 이상 = 수영
if outdoor >= 30 :
    recomend = "수영"
# 20도 이상 30도 미만 = 등산
elif 30 > outdoor >= 20 :
    recomend = "등산"
# 10도 이상 20도 미만 = 자전거 타기
elif 20 > outdoor >= 10 :
    recomend = "자전거 타기"
# 10도 미만 = 스키
elif 10 > outdoor :
    recomend = "스키"
    
print(f"현재 온도: {float(outdoor)}도")
print(f"추천 활동: {recomend}")