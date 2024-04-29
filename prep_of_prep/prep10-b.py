# 리스트에서 항목 읽기

menus = ["피자", "파스타", "샐러드", "스시", "버거"]

index = int(input("메뉴의 인덱스를 선택하세요 (0부터 시작): "))

if index > 5 or index < 0 :
    print("유효하지 않은 선택입니다.")

elif index == 0 :
    menus == "피자"
    
elif index == 1 :
    menus == "파스타"
    
elif index == 2 :
    menus == "샐러드"
    
elif index == 3 :
    menus == "스시"
    
elif index == 4 :
    menus == "버거"
    
print(f"선택된 메뉴: {menus[ind]}")