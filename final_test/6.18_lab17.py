# 단어 맞추기

# 단어 입력
# 단어를 저장할 리스트 생성
word_list = []
# 리스트 카운트 생성
count = 0
# 유효 범위를 벗어나지 않은 단어 3개를 입력받을 때 까지 반복
while count < 3:
    # 첫, 두, 세 번째를 나타내기 위한 리스트
    num_list = ["첫", "두", "세"]
    # 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
    print(f"{num_list[count]} 번째 단어를 입력 하세요")
    user_input = input()
    # 단어의 글자 범위는 5 이상, 20 이하로 제한
    if 5 > len(user_input) or len(user_input) > 20:
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
        continue
    else:
        word_list.append(user_input)
        count += 1
    # 유효 범위를 벗어난 단어를 입력할 경우, 재입력 요구


# 임시 단어
import random

# word_list = ["cczzw", "qqwwee", "aassddf"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = word_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {word_random}")
word_random = list(word_random)
# 게임 시작
# 선택된 단어의 글자 중 50%를 blind 처리
# blind 처리된 알파벳은 랜덤하게 선택
# 선택된 단어의 길이
word_lenght = len(word_random)
# 길이 절반
word_half = word_lenght / 2
# 길이 절반이 절반의 몫보다 크면, + 1
if word_half > word_lenght // 2:
    word_half += 1
word_half = int(word_half)
# 선택된 단어의 인덱스
index_list = []
for i in range(word_lenght):
    index_list.append(i)
# 기존 리스트는 정답용으로 두고, 출력용으로 값을 복사하여 하나 만든다
word_printed = word_random[:]
# 단어 전체길이 - 절반 만큼의 인덱스를 리스트에서 삭제한다
for j in range(word_lenght - word_half):
    del index_list[random.randint(0, word_half)]
# 남은 인덱스를 printed에 넣어 _로 바꾼다
for index in index_list:
    word_printed[index] = "_"

# 시도 횟수 카운트
trial_count = 1
# 모든 단어를 맞출 때 까지 반복해야 하니 while문 사용
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력받습니다
    print(f"{trial_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    print(word_printed)
    input_value = input()
    
    # blind 해제
    # 포함된 글자를 파악하기 위한 카운트 생성
    including_word = 0
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if input_value in word_random:
        for i in index_list:
            if input_value == word_random[i]:
                word_printed[i] = input_value
                including_word += 1
    # 존재하지 않을 경우 없음 메시지 출력
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
        continue
    print(f"입력한 알파벳 단어 내 포함: {including_word}글자")
    
    trial_count += 1
    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임 종료
    if word_printed == word_random:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {trial_count - 1}")
        break
    # 결과 출력
    # 게임 종료 시 시도 횟수 출력
