
# 비밀번호를 받는다
pw = input("비밀번호를 입력하세요: ")
# 비밀번호가 8자 이상이어야 한다
if len(pw) >= 8 :
    
    has_uppercase = False
    has_number = False
    for char in pw:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
    if has_uppercase and has_number == True :
        print("비밀번호가 안전합니다.")
    else:
        print("비밀번호가 안전하지 않습니다.")
    
else:
    print("비밀번호가 안전하지 않습니다.")
    
# 비밀번호엔 적어도 하나의 숫자가 있어야 한다.
# 비밀번호엔 적어도 하나의 대문자가 있어야 한다.

# 위 조건이 충족되지 않으면, 비밀번호는 안전하지 않다고 ㅎ출력한다.