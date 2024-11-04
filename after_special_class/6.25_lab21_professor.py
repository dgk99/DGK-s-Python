msg = """pos foo foo pos test pos
foo kin pos kin
dk test pos"""

# 우리가 문자라고 인식하는 패턴
# 1. 공백 2. enter
# - 현재 글자가 공백이거나 enter면 and 이전 글자가 공백이거나 enter가 아니면
# 이전 글자가 뭔지 파악하면 단어를 파악 가능
 
# 3. 마지막 단어 - 문장의 마지막 글자가 공백이나 개행문자가 아니면, 카운트에 추가



count = 0
count_line = 1
count_char = 0
count_word = 0

count_found_word = 0


prev = "" # 이전 글자를 저장하기 위한 변수

find_word = "pos"
find_word_index = 0
find_word_len = len(find_word)
find_word_pos = []

for cur in msg:
    
    if find_word[find_word_index] == cur:
        find_word_index += 1
        if find_word_index == find_word_len: # 글자를 찾았다
            count_found_word += 1
            find_word_index = 0
            find_word_pos.append(count - find_word_len + 1)
    else:
        find_word_index = 0
    
    if cur == " " or cur == "\n":
        if prev != " " or cur != "\n":
            count_word += 1
    elif count == len(msg) -1 : # 마지막 글자
        if prev != " " or cur != "\n":
            count_word += 1
    
    if cur != " " and cur != "\n":
        count_char += 1
    
    if cur == "\n":
        count_line += 1
    
    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트
    
print(f"총 문자 수: {count}")
print(f"총 줄 수: {count_line}")
print(f"총 글자 수: {count_char}")
print(f"총 단어 수: {count_word}")
print(f"검색된 단어 수: {count_found_word}")
print(f"검색된 단어 위치: {find_word_pos}")

