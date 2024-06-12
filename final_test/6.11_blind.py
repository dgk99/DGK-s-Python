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
random_word = com_list[random.randint(0, 2)]

# 게임 시작
# 선택된 단어의 글자 중 50%를 blind처리
# blind 처리된 알파벳은 랜덤하게 선택
# 선택된 단어의 길이
word_length = len(random_word)
# 선택된 단어의 길이의 절반
half_lenght = word_length / 2
# 만약 선택된 단어의 절반이 절반의 몫보다 크면, 0.5 더하기
if half_lenght > word_length // 2:
    half_lenght += 0.5
half_lenght = int(half_lenght)
print(half_lenght)
# 선택된 단어를 리스트에 넣기
word_list = list(random_word)
print(word_list)
# 선택된 단어의 인덱스를 나타내는 인덱스 리스트 만들기
index_list = []
for index in range(len(word_list)):
    index_list.append(index)
print(index_list)
# 이 중에서 절반 만큼 삭제하기
for i in range(half_lenght):
    del index_list[random.randint(0, len(index_list) - 1)]
print(index_list)
# word_list는 정답용, 출력용 리스트를 만들어 값을 복사
word_printed = word_list[:]
# 출력용 리스트에서 절반 값을 삭제 후 _ 삽입
# for j in index_list:
#     if j != 

# 알파벳 입력
# 키보드로부터 알파벳 한 글자를 입력받음

# blind 해제
# 입력받은 알파벳이 단어 내 존재할 경우 blind 해제
# 존재하지 않을 경우 "없음" 메시지 출력

# 게임 종료
# 단어의 모든 글자를 맞출 경우 게임이 종료

# 결과 출력
# 게임 종료 시 시도 횟수를 출력