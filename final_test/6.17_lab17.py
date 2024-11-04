# 단어 맞추기 게임

# 단어 입력
# 입력받은 단어를 저장할 리스트
input_list = []
# 3개의 단어를 받았다는 걸 확인하기 위한 카운트 생성
count = 0
# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구하니 while문 사용
while count < 3:
    # 첫, 두, 세 숫자를 나타내기 위한 리스트
    num_list = ["첫", "두", "세"]
    # 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
    print(f"{num_list[count]} 번째 단어를 입력 하세요")
    user_input = input()
    # 단어의 글자 범위는 5 이상, 20 이하로 제한
    if 5 > len(user_input) or len(user_input) > 20:
        print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
        continue
    else:
        input_list.append(user_input)
        count += 1


# 임시 리스트
import random

# input_list = ["cceew", "qqwwee", "zzxxccv"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = input_list[random.randint(0, 2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {word_random}")
word_random = list(word_random)

# 게임 시작
# 선택된 단어의 길이
word_lenght = len(word_random)
# 선택된 길이의 절반
word_half = word_lenght / 2
# 만약, word_half가 word_length // 2 보다 크면, + 1
if word_half > word_lenght // 2:
    word_half += 1
word_half = int(word_half)
# word_random의 index list 생성
index_list = []
for i in range(word_lenght):
    index_list.append(i)
# index_list에서 word_length - word_half만큼 뺀 값을 삭제한다
for index in range(word_lenght - word_half):
    del index_list[random.randint(0, word_half)]
# word_random은 정답용, 출력용으로 새 리스트를 만들어 값을 복사한다.
word_printed = word_random[:]
# 남은 index_list의 값을 word_printed에 넣어 _로 바꿔준다
for i in index_list:
    word_printed[i] = "_"
# 선택된 단어의 글자 중 50%를 blind 처리
# blind 처리된 알파벳은 랜덤하게 선택

# 시도 카운트
num_count = 1
# 모든 단어를 맞출 때 까지 반복해야 하니 while문 사용
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력
    print(f"{num_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{word_printed}")
    word_input = input()
    # blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if word_input in word_random:
        for j in index_list:
            if word_random[j] == word_input:
                word_printed[j] = word_input
    # 존재하지 않을 경우 없음 메시지 출력
    else: 
        print("단어 내 포함되지 않은 알파벳입니다.")
    num_count += 1

    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_random == word_printed:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {num_count - 1}")
        break

    # 결과 출력
    # 게임 종료 시 시도 횟수를 출력
