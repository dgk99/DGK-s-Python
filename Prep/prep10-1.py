# 학교 도서관을 위한 프로그램 작성
# 도서제목을 입력하면 해당 제목을 도서 목록에 추가하는 기능을 만들어야 한다.
# 사용자가 종료 라고 입력할 때 까지 이 프로세스를 반복하고 마지막에 전체 도서 목록을 출력하라.

books = []

while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    if title == '종료':
        break
    books.append(title)
    
print("도서 목록:", books)