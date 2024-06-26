# 문자열 검색 프로그램

# • 요구사항:
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 1. 미리 입력된 문장에서 검색 문자열을 입력 받고,
# 2. 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# 3. 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받는다

# 모든 문자 카운트
count_all = 0
# 전체 문자 수 카운트
count_total = 0
# 줄 수 카운트
count_line = 1

# 단어를 찾기위한 조건들
word_list = []
word = ""

# • 기능 상세

# – 문자열 검색
while True:
    # ① 입력 받은 문자열이 문장 내 있을 경우
    user_input = input("검색할 문자열을 입력하세요: ")
    if user_input not in sentence:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
    else:
        
    #  검색된 문자열에 대한 정보를 출력
        for i in sentence:
            count_all += 1
        # » 검색된 문자열의 개수

        # » 검색된 문자열의 위치(들)
        # • 위치는 문자열이 시작되는 인덱스를 기준으로 하며, 문장의 첫 번째 글자는 인덱스 0으로 한다
        # • 예를 들어, "hello world"에서 "o"를 검색하면, 위치는 [4, 7]로 출력

        #  전체 문장에 대한 정보를 출력
        # » 단어의 개수 (단어는 띄어쓰기로 구분)
            if i != " " and i != "\n":
                word = word + i
            
            elif count_all - len(sentence) -1:
                word_list.append(word)
            
            else:
                word_list.append(word)
                word = ""
            
                
                
        # » 전체 문자 수(공백과 개행 문자를 제외한 글자 수)
            if i != " " and i != "\n":
                count_total += 1
        # » 줄 수 (The number of lines)
            if i == "\n":
                count_line += 1

        # ② 입력 받은 문자열이 문장 내 없을 경우
        # – 해당 문자열이 없음을 화면에 출력하고, 검색할 문자열을 재입력 받는다
        # – 검색된 문자열이 있을 때 까지 반복한다

    print(f"전체 문자 수: {count_total}")
    print(f"줄 수: {count_line}")
    print(word_list)
