# 비밀번호 검증기

# 비밀번호 입력받기
password = input("비밀번호를 입력하세요: ")

# 비밀번호는 8자 이상
if len(password) >= 8 :
    
    has_number = False
    has_uppercase = False
    
    for char in password :
        if char.isdigit():
            has_number = True
        elif char.isupper():
            has_uppercase = True
    if has_uppercase and has_number == True :
        print("비밀번호가 안전합니다.")
    else:
        print("비밀번호가 안전하지 않습니다.")
else:
    print("비밀번호가 안전하지 않습니다.")
# 비밀번호엔 적어도 하나의 숫자 포함
# 비밀번호엔 적어도 하나의 대문자 포함
# 조건에 충족하면 비밀번호가 안전합니다 출력

# 그렇지 않을 때는 비밀번호가 안전하지 않습니다 출력