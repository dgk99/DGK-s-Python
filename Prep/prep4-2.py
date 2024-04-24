# 비밀번호가 안전한지 확인하는 프로그램
# 비밀번호의 조건
# 1. 비밀번호는 8자 이상 이어야 한다.
# 2. 비밀번호에는 최소 하나의 숫자가 포함되어야 한다.
# 3. 비밀번호에는 최소 하나의 대문자가 포함되어야 한다.

# 위 3개가 다 충족되지 않으면, 비밀번호는 안전하지 않다(False)

# 위 3개가 다 충족되면, 비밀번호가 안전하다 라고 출력한다.

# 일단 비밀번호를 입력받는다
password = input("비밀번호를 입력하세요: ")
# 먼저 비밀번호가 최소 8자가 되어야 한다.

has_number = False
has_uppercase = False

for char in password :
    if char.isdigit():
        has_number = True
        break


for char in password :
    if char.isupper():
        has_uppercase = True
        break

if len(password) >= 8 and has_number and has_uppercase :
    print("비밀번호가 안전합니다.")
else:
    print("비밀번호가 안전하지 않습니다.")


    
