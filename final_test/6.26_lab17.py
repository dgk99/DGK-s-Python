# 단어 맞추기 게임

# 단어 저장 리스트
import random


# word_list = []
# # 리스트에 3 단어가 들어갈 때 까지 반복
# while len(word_list) < 3:
#     # 1. 단어 입력
#     # 첫 두 세 를 나타내는 리스트
#     num_list = ["첫", "두", "세"]
#     # • 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
#     print(f"{num_list[len(word_list)]} 번째 단어를 입력 하세요")
#     word_input = input()
#     # • 단어의 글자 범위는 5 이상, 20 이하로 제한됩니다.
#     if len(word_input) < 5 or 20 < len(word_input):
#         print("5이상 20이하 글자로 구성된 단어를 입력 하세요")        
#     # • 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다.
#     else:
#         word_list.append(word_input)
# print(word_list)

# 임시 리스트
word_list = ["qqwwe", "aassdd", "zzxxccv"]

# 2. 단어 선택
# • 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
random_word = word_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {random_word}")
random_word = list(random_word)
# 3. 게임 시작
# 선택된 단어의 길이
word_len = len(random_word)
# 선택된 단어의 절반
word_half = word_len / 2
# 절반이 몫보다 크면 + 1
if word_half > word_len // 2:
    word_half += 1
word_half = int(word_half)

# 선택된 단어의 인덱스 리스트
index_list = [value for value in range(word_len)]

# 총 길이 - 절반 만큼 삭제
for _ in range(word_len - word_half):
    del index_list[random.randint(0, word_half)]
# 출력용 리스트 생성
printed_word = random_word[:]
# 남은 index를 _로 바꾸기
for index in index_list:
    printed_word[index] = "_"
# • 선택된 단어의 글자 중 50%를 Blind 처리합니다.
# • Blind 처리된 알파벳은 랜덤하게 선택됩니다.

# 시도 횟수 카운트
game_count = 1
# 단어 내에 포함되어 있나 나타내는 카운트
in_word = 0
# 조건에 만족할 때 까지 반복
while True:
    # 4. 알파벳 입력
    # • 키보드로부터 알파벳 한 글자를 입력받습니다.
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{printed_word}")
    user_input = input()
    # 5. Blind 해제
    # • 입력받은 알파벳이 단어 내에 존재할 경우 Blind를 해제합니다.
    if user_input in random_word:
        for i in index_list:
            if random_word[i] == user_input:
                in_word += 1
                printed_word[i] = user_input
        print(f"입력한 알파벳 단어 내 포함: {in_word}글자")
    # • 존재하지 않을 경우 “없음” 메시지를 출력합니다
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    in_word = 0
    game_count += 1
        
    # 6. 게임 종료
    # • 단어의 모든 글자를 맞출 경우 게임이 종료됩니다
    if random_word == printed_word:
        print(f"Clear - 선택된 단어: {random_word}, 총 시도 횟수: {game_count - 1}")
        break
    # 7. 결과 출력
    # • 게임 종료 시 시도 횟수를 출력합니다