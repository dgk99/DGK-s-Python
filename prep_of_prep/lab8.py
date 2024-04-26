# 영문 모음 판별기

# 사용자에게 하나의 영문자를 입력받고, 해당 문자가 모음(a, e, i, o, u) 중
# 하나인지 아닌지를 판별하여 출력하는 프로그램 작성

# 사용자에게 하나의 문자를 입력받습니다.
alphabet = input("한 문자를 입력하세요: ")
# 입력받은 문자가 모음인지 아닌지 확인합니다.
if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u" :
    print(alphabet,"는 모음입니다.")
else:
    print(alphabet,"는 모음이 아닙니다.")
# 결과를 출력합니다.