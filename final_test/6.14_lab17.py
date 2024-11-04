# 단어 맞추기 게임

# 단어 입력
# 키보드로부터 영어 단어 3개를 입력받아 리스트에 저장
# 단어의 글자 범위는 5이상 20이하
# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구

# 임시 단어
import random
com_list = ["ddiie", "kkqqaa", "zzcclli"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = com_list[random.randint(0, 2)]
word_random = list(word_random)
print(word_random)

# 게임 시작
# 선택된 단어의 글자 중 50%를 blind 처리
# blind 처리된 알파벳은 랜덤하게 선택

# 선택된 단어의 길이
word_length = len(word_random)
print(word_length)
# 선택된 단어 길이의 절반
half = word_length / 2
# 만약 길이 절반이 절반의 몫보다 크면, 0.5 더하기
if half > word_length // 2:
    half += 1
half = int(half)
print(half)
# word_random의 index를 리스트에 저장
index_list = []
for index in range(word_length):
    index_list.append(index)
print(index_list)
# 이 중에서 절반만 남기고 삭제
for i in range(word_length - half):
    del index_list[random.randint(0, half)]
print(index_list)
# word_random을 정답용으로 두고, 출력용으로 같은 값의 리스트를 복사한다.
word_printed = word_random[:]
print(word_printed)
# 이 복사한 리스트에 index값을 넣어 _로 바꾼다
for index in index_list:
    word_printed[index] = "_"
print(word_printed)

# 번째 시도 카운트
count = 1
# 모든 알파벳을 맞출 때 까지 진행되어야 하니 while문 사용
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력받는다.
    user_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n")
    
    # blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if user_input in word_random:
        for i in index_list:
            if user_input == word_random[i]:
                word_printed[i] = user_input
        print(word_printed)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    # 존재하지 않을 경우 없음 메시지 출력
    
    count += 1

    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_random == word_printed:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count}")