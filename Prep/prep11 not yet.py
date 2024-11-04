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