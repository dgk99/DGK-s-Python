# 사전 예약 시스템 시뮬레이터


# 잘못된 입력: 잘못된 입력입니다. 프로그램을 종료합니다.

    
# 입력받아야 할 정보
# 사용자의 나이
age = int(input("나이를 입력하세요: "))
eventcode = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))
# 이벤트 코드 = E1, E2, E3 중 하나만 가능
# 날짜 = 1~30만 가능

# 이벤트 코드
# E1 = 만 18세 이상만 가능
# E2 = 모든 연령대가 가능, 날짜는 짝수만
# E3 = 만 16세 이상만 가능, 7의 배수에만 가능

# 잘못된 입력: 잘못된 입력입니다. 프로그램을 종료합니다.
if eventcode != "E1" and eventcode != "E2" and eventcode != "E3" :
        print("잘못된 입력입니다. 프로그램을 종료합니다")
elif reservation_date > 30 or reservation_date < 1 :
        print("잘못된 입력입니다. 프로그램을 종료합니다")
elif eventcode == "E1" and age < 18 :
        print("나이 제한으로 인해 예약할 수 없습니다.")
elif eventcode == "E3" and age < 16 :
        print("나이 제한으로 인해 예약할 수 없습니다.")
elif eventcode == "E2" and reservation_date % 2 != 0 :
        print("선택하신 날짜에는 예약할 수 없습니다.")
elif eventcode == "E3" and reservation_date % 7 != 0 :
        print("선택하신 날짜에는 예약할 수 없습니다.")
else:
        print("예약이 완료되었습니다!")
# 예약 성공: 예약이 완료되었습니다.
# 나이 미달: 나이 제한으로 인해 예약할 수 없습니다.
# 날짜 제한: 선택하신 날짜에는 예약할 수 없습니다.
