# 문자열 검색 프로그램

# 문자열 검색을 위한 사전 입력 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 문자열에 \n을 공백으로 치환
sentence_del_n = sentence.replace("\n", " ")
sentence_del_n = sentence_del_n.split(" ")

# 문자열 개수를 파악할 카운트
num_word_count = 0
# 전체 단어 갯수 카운트
word_count = 0
# 전체 문자 갯수를 세기 위해 공백과 \n을 세는 카운트
blank_n_count = 0
# 줄 수 카운트
line_count = 1

# 미리 입력된 문장에서 검색 문자열을 입력 받고,
# 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받는다

while True:
    user_input = input("검색할 문자열을 입력하세요: ")
    # 입력값이 문자열에 포함되어 있다면
    if user_input in sentence:
        # 문자열의 개수 파악하는 반복문
        for word_num in sentence_del_n:
            if word_num == user_input:
                num_word_count += 1
        print(f"검색된 문자열의 개수: {num_word_count}")
        
        # 문자열의 위치 파악하는 조건문
        user_list = []
        user_list += user_input
        total = list(sentence)
        location_list = []
        location_count = 0
        for i in total:
            if user_list[0] == i:
                location_list.append(location_count)
            location_count += 1
        print(f"검색된 문자열의 위치: {location_list}")
        # 단어의 개수 조건문
        for i in sentence_del_n:
            if i != "":
                word_count += 1
        print(f"단어의 개수: {word_count}")
        
        # 전체 문자 수 (총 길이에서 공백과 \n을 뺀 값)
        
        for word in total:
            if word == ' ' or word == "\n":
                blank_n_count += 1
        print(f"전체 문자 수: {len(total) - blank_n_count}")
        
        # 줄 수 조건문
        for line in total:
            if line == "\n":
                line_count += 1
        print(f"줄 수: {line_count}")
        break
    # 입력값이 문자열에 포함되어 있지 않다면
    else:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        continue
        

# 입력받은 문자열이 문장 내 있을 경우
# 검색된 문자열에 대한 정보를 출력
# 검색된 문자열의 개수
# 검색된 문자열의 위치(들)
# 위치는 문자열이 시작되는 인덱스를 기준으로 하며, 문장의 첫 번째 글자는 인덱스 0으로 한다
# 예를 들어, "hello world"에서 "o"를 검색하면 위치는 [4, 7]로 출력

# 전체 문장에 대한 정보를 출력
# 단어의 개수 (단어는 띄어쓰기로 구분)
# 전체 문자 수(공백과 개행 문자를 제외한 글자 수)
# 줄 수(The number of lines)

# 입력 받은 문자열이 문장 내 없을 경우
# 해당 문자열이 없음을 화면에 출력하고, 검색할 문자열을 재입력 받는다
# 검색된 문자열이 있을 때 까지 반복한다.