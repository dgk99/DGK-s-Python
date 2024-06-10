import random

# 사용자로부터 5글자 이상 20글자 이하의 단어 3개 입력받기
words_list = []
x = 0

# 올바른 단어 3개를 받을 때까지 반복
while len(words_list) < 3:
    for i in range(3 - len(words_list)):
        word = input(f"{x+1} 번째 단어를 입력 하세요: ")
        if 5 <= len(word) <= 20:
            words_list.append(word)
            x += 1
        else:
            print("5이상 20이하 글자로 구성된 단어를 입력 하세요.")

# 단어 목록에서 무작위로 단어 선택
word_selected = list(words_list[random.randint(0, 2)])
word_printed = word_selected[:]

print("단어 선택 완료 게임을 시작합니다.")

# 선택된 단어의 글자 수
char_num_word = len(word_selected)

# 글자 수의 절반을 블라인드 처리
blind_num_word = char_num_word // 2 + char_num_word % 2

# 블라인드 처리할 인덱스 목록 생성
list_blind_index = random.sample(range(char_num_word), blind_num_word)

# 선택된 인덱스를 블라인드 처리
for index in list_blind_index:
    word_printed[index] = "_"

print(f"블라인드 처리된 단어: {word_printed}")

# 글자를 맞추는 게임 루프
count = 1
while "_" in word_printed: 
    input_value = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.: ")

    if len(input_value) != 1:
        print("한 단어만 입력하세요.")
        continue

    # 맞춘 글자를 단어에 표시
    blind_index_length = len(list_blind_index)
    list_blind_index = [index for index in list_blind_index if word_selected[index] != input_value]

    # 표시된 글자 업데이트
    for index in range(char_num_word):
        if word_selected[index] == input_value:
            word_printed[index] = input_value

    # 맞춘 경우와 틀린 경우에 대한 피드백
    if blind_index_length != len(list_blind_index):
        print(word_printed)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    count += 1

print(f"Clear - 선택된 단어: {word_printed}, 총 시도 횟수: {count-1}")