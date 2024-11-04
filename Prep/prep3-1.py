# 나이, 이벤트 코드, 날짜를 입력받는다
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 이벤트 코드와 날짜를 잘못 입력햇다 안햇다로 나눈다
if event_code != "E1" and event_code != "E2" and event_code != "E3":
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
elif reservation_date < 1 or reservation_date > 30 :
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    # 나이가 미달이다 아니다로 나뉜다
elif event_code == "E1" and age < 18:
    print("나이 제한으로 인해 예약할 수 없습니다.")
elif event_code == "E3" and age < 16:
    print("나이 제한으로 인해 예약할 수 없습니다.")
        # 날짜가 홀수거나 7의 배수가 아니면 할수없다로 거른다
elif event_code == "E2" and reservation_date % 2 != 0:
    print("선택하신 날짜에는 예약할 수 없습니다.")
elif event_code == "E3" and reservation_date % 7 != 0:
    print("선택하신 날짜에는 예약할 수 없습니다.")

else:
    print("예약이 완료되었습니다!")