# 단어 맞추기 게임

# 단어 입력
# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
# 단어의 글자 범위는 5 이상 20 이하로 제한
# 유효 범위를 벗어난 단어를 입력할 경우 재입력 요구

# 임시 단어
import random


com_list = ["zzcce", "qqeerr", "iikknna"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = com_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {word_random}")
word_random = list(word_random)
# 게임 시작
# 선택된 단어의 글자 중 50%를 blind 처리
# 선택된 단어의 길이
word_random_length = len(word_random)
print(word_random_length)
# 단어 길이 절반
half = word_random_length / 2
# 만약 절반이 길이//2 보다 크면 += 1
if half > word_random_length // 2:
    half += 1
half = int(half)
print(half)
# 선택된 단어의 index를 리스트로 생성
index_list = [int(value) for value in range(0, word_random_length)]
print(index_list)
# 이 index list에서 총 길이 - 절반만큼 index를 삭제
for i in range(word_random_length - half):
    del index_list[random.randint(0, half)]
print(index_list)
# word_random은 정답용, 그 값을 복사해서 출력용으로 리스트를 만들어 준다.
word_printed = word_random[:]
# word_printed에 index list에 대당하는 부분을 _로 바꾼다
for index in index_list:
    word_printed[index] = "_"
print(word_printed)
# blind 처리된 알파벳은 랜덤하게 선택

# 시도 카운트
count = 1
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력받는다
    print(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{word_printed}")
    user_input = input()
    # blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if user_input in word_random:
        for i in index_list:
            if user_input == word_random[i]:
                word_printed[i] = user_input
                
    else:
        print("단어 내 포함하지 않은 알파벳입니다.")
    count += 1
    # 존재하지 않을 경우 없음 메시지 출력

    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_printed == word_random:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count}")
        break

    # 결과 출력
    # 게임 종료 시 시도 횟수를 출력