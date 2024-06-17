# 단어 맞추기 게임

# 단어 입력
# 플레이어가 입력한 단어를 저장할 리스트
import random

# user_list = []
# # 저장된 단어의 갯수를 알려주는 count 생성
# count = 0
# # 단어 3개가 저장될 때 까지 반복해야 하니 while문 사용
# while count < 3:
#     # 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
#     # 첫, 두, 세 글자를 나타내기 위해 리스트 생성
#     num_list = ["첫", "두", "세"]
#     # 플레이어에게 키보드로부터 영어 단어 입력받기
#     print(f"{num_list[count]} 번째 단어를 입력하세요")
#     user_input = input()
#     # 단어의 글자 범위는 5 이상 20 이하로 제한
#     if 20 >= len(user_input) >= 5:
#         user_list.append(user_input)
#         count += 1
#     # 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구
#     else:
#         print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
#         continue
    
# 임시 단어
user_list = ["kkeei", "aazzcc", "iiooppq"]    

# 종료 조건을 만족할 때 까지 반복해야 하니 while문 사용

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = user_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {word_random}")
word_random = list(word_random)
# 게임 시작
# 선택된 단어의 글자 중 50%를 blind 처리합니다.
# 선택된 단어의 길이
word_length = len(word_random)
print(word_length)
# 선택된 단어의 길이 절반
word_half = word_length / 2
print(word_half)
# 만약, 길이 절반이 총 길이의 절반 몫 보다 크면 + 1
if word_half > word_length // 2:
    word_half += 1
word_half = int(word_half)
print(word_half)
# word_random은 정답용으로 두고, 출력용으로 쓸 리스트 생성해 word_random값 복사
word_printed = word_random[:]
# 선택된 단어의 index값을 넣을 리스트
index_list = []
# index값 생성 후 리스트에 저장
for i in range(word_length):
    index_list.append(i)
print(index_list)
# 총 길이 - 절반 만큼 빼고 그 나머지를 삭제
for i in range(word_length - word_half):
    del index_list[random.randint(0, word_half)]
print(index_list)
# blind 처리된 알파벳은 랜덤하게 선택
# 남은 index를 대입해서 _로 바꾸기
for index in index_list:
    word_printed[index] = "_"
print(word_printed)

# 시도 횟수 카운트
count = 1
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력
    alphabet_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    print(word_printed)

    # blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if alphabet_input in word_random:
        for i in index_list:
            if alphabet_input == word_random[i]:
                word_printed[i] = alphabet_input
        print(word_printed)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
        continue
    count += 1
    # 존재하지 않을 경우 없음 메시지 출력

    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_printed == word_random:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count}")
        break

    # 결과 출력
    # 게임 종료 시 시도 횟수를 출력