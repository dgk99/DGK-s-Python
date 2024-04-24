# 사용자로부터 현재 온도(섭씨)를 입력받습니다.
celsius = int(input("현재 온도(섭씨)를 입력하세요: "))
# 입력받은 온도에 따라 적합한 야외 활동을 추천하세요.
# 온도 범위에 따른 활동추천은 다음과 같습니다.
# 30도 이상: 수영
if celsius >= 30 :
    print(f"현재 온도: {float(celsius)}도")
    print("추천 활동: 수영")
elif 30 >= celsius >= 20 : # 20도 이상 30도 미만: 등산
    print(f"현재 온도: {float(celsius)}도")
    print("추천 활동: 등산")
elif 20 >= celsius >= 10 : # 10도 이상 20도 미만: 자전거 타기
    print(f"현재 온도: {float(celsius)}도")
    print("추천 활동: 자전거 타기")
else: # 10도 미만: 스키
    print(f"현재 온도: {float(celsius)}도")
    print("추천 활동: 스키")



