# 점심 메뉴 정하기 프로그램
# 사용자가 유효하지 않은 인덱스를 입력하면, '유효하지 않은 선택입니다'라고 출력

# 미리 정의된 메뉴 리스트가 있고,
menus = ["피자", "파스타", "샐러드", "스시", "버거"]

# 사용자에게 인덱스 번호를 받아 해당 인덱스의 메뉴를 출력하는 프로그램 작성
index = int(input("메뉴의 인덱스를 선택하세요 (0부터 시작): "))

if index >= 0 and index < 5 :
    print("선택한 메뉴 :", menus[index])
else:
    print("유효하지 않은 선택입니다.")
    
    