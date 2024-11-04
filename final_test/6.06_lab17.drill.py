# 단어 맞추기 게임

# 단어 입력
# 단어를 저장할 리스트 생성
word_list = []
# # 첫, 두, 세 번째 로 출력할 단어 리스트
# number_list = ["첫", "두", "세"]
# 리스트가 3이 되기전까지 작동하는 카운트 만들기
count = 1
# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
while count < 4: # 리스트의 길이가 3보다 작을 때만 작동하는 조건문
    print(f"{count} 번째 단어를 입력 하세요")
    user_input = input()
    # 단어의 글자 범위는 5 이상, 20자 이하로 제한됩니다.
    if 5 <= len(user_input) <= 20:
        word_list.append(user_input)
        count += 1
    else: # 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다.
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
# print(word_list)

# 단어 선택
import random
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택합니다.
random_word = random.choice(word_list)
print(f"단어 선택 완료 \n게임을 시작합니다.\n선택된 단어: {random_word}")

# 게임 시작
# 선택된 단어의 글자 중 50%선택
# 예를 들어, 선택된 단어가 starbucks인 경우, 글자수는 9자입니다.
# 9/2 = 4.5d이므로 올림해서 5자를 blind 처리합니다.
# 올림 알고리즘은 직접 구현하며, 이를 위한 함수를 사용하지 마세요.
half = len(random_word) / 2
if half % 2 < 1:
    half += 0.5
half = int(half)

# 선택된 단어의 50%를 블라인드로 처리
# blind 처리된 알파벳은 랜덤하게 선택됩니다.
# random_word에서 half만큼 blind 처리를 하기위해 랜덤으로 half만큼 고른다

choice_word = random.randint(0, half)
print(choice_word)

# 알파벳 입력
# 키보드로부터 알파벳 한 글자를 입력받습니다.

# blind 해제
# 입력받은 알파벳이 단어 내에 존재할 경우 blind를 해제합니다.

# 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료됩니다.

# 결과 출력
# 게임 종료 시 시도 횟수를 출력합니다.