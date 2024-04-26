# 사용자로부터 길이를 입력 받아 해다 길이의 무작위 패스워드를 생성하는 함수
# generate_password(length)를 구현합니다.
# 이 함수는 대문자, 소문자, 숫자를 조합하여 패스워드를 생성해야 합니다.

import random

def generate_password(length):
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    all_characters = uppercase_letters + lowercase_letters + digits
    
    password = ""
    
    for _ in range(length):
        password +=random.choice(all_characters)
        
    return password

generated_password = generate_password(8)
print(generated_password)