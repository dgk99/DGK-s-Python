# 사용자로부터 하나의 영문자를 입력받고, 해당 문자가 모음(a, e, i, o, u) 중 하나인지 아닌지를 판별하여 결과를 출력하는 프로그램을 만들어라
# 사용자에게 영문자 하나를 입력받는다.
alphabet = input("한 문자를 입력하세요: ")

# 사용자가 입력한 영문자가 a일 경우, a는 모음입니다 라고 출력한다
if alphabet == "a":
    print(alphabet,"는 모음입니다.")

# 사용자가 입력한 영문자가 e일 경우, e는 모음입니다 라고 출력한다
elif alphabet == "e":
    print(alphabet,"는 모음입니다.")

# 사용자가 입력한 영문자가 i일 경우, i는 모음입니다 라고 출력한다
elif alphabet == "i":
    print(alphabet,"는 모음입니다.")
    
# 사용자가 입력한 영문자가 o일 경우, o는 모음입니다 라고 출력한다
elif alphabet == "o":
    print(alphabet,"는 모음입니다.")

# 사용자가 입력한 영문자가 u일 경우, u는 모음입니다 라고 출력한다
elif alphabet == "u":
    print(alphabet,"는 모음입니다.")
    
# 그렇지 않은 나머지 영문자를 입력했을시, 모음이 아닙니다 라고 출력한다
else:
    print(alphabet,"는 모음이 아닙니다.")