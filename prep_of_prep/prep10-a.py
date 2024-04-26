# 리스트에 항목 추가하기

books = []

while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    
    if title == '종료' :
        break
    books.append(title)
    
    
print("도서 목록: ", books)