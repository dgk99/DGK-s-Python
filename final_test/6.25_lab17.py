# 단어 맞추기 게임

# 입력한 단어를 저장할 리스트
import random


word_list = []
# 3개의 단어가 저장되는 걸 확인하는 카운트
count = 0
# 유효 범위의 단어가 3개 저장될 때 까지 반복해야 하니 while문 사용
while count < 3:
    # 1. 단어 입력
    # 첫, 두, 세 가 담긴 리스트
    num_list = ["첫", "두", "세"]
    # • 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
    print(f"{num_list[count]} 번째 단어를 입력 하세요")
    word_input = input()
    if len(word_input) > 20 or len(word_input) < 5:
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
        continue
    # • 단어의 글자 범위는 5 이상, 20 이하로 제한됩니다.
    # • 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다.
    else:
        word_list.append(word_input)
        count += 1

# 임시 단어


# 2. 단어 선택
# • 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
random_word = word_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {random_word}")
random_word = list(random_word)
# 3. 게임 시작
# 선택된 단어의 길이
r_word_len = len(random_word)
# 선택된 단어의 절반
r_word_half = r_word_len / 2
# 단어의 절반이 r_word_len // 2 보다 크면 + 1
if r_word_half > r_word_len // 2:
    r_word_half += 1
r_word_half = int(r_word_half)

# • 선택된 단어의 글자 중 50%를 Blind 처리합니다.
# 선택된 단어의 총 길이 index
index_list = [int(value) for value in range(0, r_word_len)]

# 이 중에서 총 길이 - 절반 만큼 삭제
for _ in range(r_word_len - r_word_half):
    del index_list[random.randint(0, r_word_half)]

# random_word는 정답용, printed_word는 출력용으로 해서 _로 바꿔준다
printed_word = random_word[:]
# • Blind 처리된 알파벳은 랜덤하게 선택됩니다
for index in index_list:
    printed_word[index] = "_"

# 시도 횟수 카운트
game_count = 1
# 단어 내 포함 카운트
word_in = 0

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
                word_in += 1
                printed_word[i] = user_input
        print(f"입력한 알파벳 단어 내 포함: {word_in}글자")
        
        word_in = 0
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
        
    
    game_count += 1
    # • 존재하지 않을 경우 “없음” 메시지를 출력합니다
    # 6. 게임 종료
    # • 단어의 모든 글자를 맞출 경우 게임이 종료됩니다
    if random_word == printed_word:
        print(f"Clear - 선택된 단어: {random_word}, 총 시도 횟수: {game_count - 1}")
        break
    # 7. 결과 출력
    # • 게임 종료 시 시도 횟수를 출력합니다