# 단어 맞추기 게임

# 단어 입력
# 키보드로부터 영어 단어 3개를 입력받아 리스트에 저장
# 단어의 글자 범위는 5 이상 20 이하로 제한
# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구

# 임시 단어
import random

com_list = ["kkiikk", "jjooe", "bbaacce"]

# 단어 선택
# 입력된 단어 중 한개의 단어를 임의로 선택
word_random = com_list[random.randint(0, 2)]
word_random = list(word_random)
print(word_random)
# 게임 시작
# 선택된 단어의 글자 중 50%를 blind처리
# 선택된 단어의 글자 길이
word_lenght = len(word_random)
# 선택된 단어의 글자 길이 절반
word_half = word_lenght / 2
# 만약 단어 길이의 절반이 몫보다 크면, +0.5
if word_half > word_lenght // 2:
    word_half += 0.5
print(word_half)
# 선택된 단어의 길이 인덱스 리스트
word_index_list = []
for index in range(0, word_lenght):
    word_index_list.append(index)
print(word_index_list)
word_half = int(word_half)
# 이 인덱스 리스트에서 선택 단어 길이 - 선택 단어 절반
for i in range(word_lenght - word_half):
    del word_index_list[random.randint(0, word_half)]
print(word_index_list)
# word_random의 값을 복사한 새 리스트 생성
word_printed = word_random[:]
# word_printed의 값을 _로 변경
for index in word_index_list:
    word_printed[index] = "_"
print(word_printed)

# 알파벳 입력
# 키보드로부터 알파벳 한 글자를 입력받음
# 시도 카운트 생성
count = 1
# 모든 알파벳을 맞출 때 까지 진행되야 하니 while문 사용
while True:
    user_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요\n")
    
    # blind 해제
    # 입력받은 알파벳이 단어 내 존재할 경우 blind 해제
    if user_input in word_random:
        for j in word_index_list:
            if user_input == word_random[j]:
                word_printed[j] = user_input 
        print(word_printed)
    # 존재하지 않을 경우 "없음" 메시지 출력
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    
    count += 1

# 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_random == word_printed:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count - 1}")
        break

# 결과 출력
# 게임 종료 시 시도 횟수를 출력