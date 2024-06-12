# 단어 맞추기 게임

# 단어를 저장할 리스트 생성
word_list = []
# # 첫, 두, 세 번째 로 출력할 단어 리스트
# number_list = ["첫", "두", "세"]
# 리스트가 3이 되기전까지 작동하는 카운트 만들기
count = 1
# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장합니다.
# while count < 4: # 리스트의 길이가 3보다 작을 때만 작동하는 조건문
#     print(f"{count} 번째 단어를 입력 하세요")
#     user_input = input()
#     # 단어의 글자 범위는 5 이상, 20자 이하로 제한됩니다.
#     if 5 <= len(user_input) <= 20:
#         word_list.append(user_input)
#         count += 1
#     else: # 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구합니다.
#         print("5이상 20이하 글자로 구성된 단어를 입력 하세요")

# 임시 단어
import random
word_list = ["kkkio", "ppeeri", "jjaappe"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
random_word = word_list[random.randint(0, 2)]
random_word = list(random_word)

# 게임 시작
# 먼저 선택된 단어의 길이 확인
random_word_len = len(random_word)
print(random_word_len)
# 길이의 절반을 구한다
random_word_half = random_word_len / 2
# // 2 + % 2
# 만약 이 절반이 절반의 몫보다 크면, 0.5을 더한다
if random_word_half > random_word_len // 2:
    random_word_half += 0.5

# blind 처리된 알파벳은 랜덤하게 선택
# random_word는 정답으로 두고, 이 값을 복사한 리스트를 하나 만든다
new_list = random_word[:]
print(new_list)

# new_list의 index list를 만든다
index_list = []
# index_list 안에 0부터 random_word의 길이만큼 index 값을 넣어준다
for i in range(0, int(random_word_len)):
    index_list.append(i)

# 이 중에서 random_word의 절반만큼 index값을 삭제한다
for i in range(int(random_word_len - random_word_half)):
    del index_list[random.randint(0, len(index_list) - 1)]
print(index_list)

# 랜덤한 인덱스의 절반을 블라인드 처리
for index in index_list:
    new_list[index] = "_"
print(new_list)

# 알파벳 입력
# 시도 카운트
count = 1
# 빈칸을 모두 채울 때 까지 입력받아야 하니 while문 사용
while True:
    if new_list == random_word:
        print(f"Clear - 선택된 단어: {random_word}, 총 시도 횟수: {count - 1}")
        break
    
    # 키보드로부터 알파벳 한 글자를 입력받음
    input_value = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요: ")
    
    
    
    # 이 값이 블라인드된 값과 동일한지 체크
    if input_value in random_word:
        for j in index_list:
            if input_value == random_word[j]:
                new_list[j] = input_value
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    
    print(new_list)
    count += 1
    
    
    
            
    
        # blind 해제
        # 입력받은 알파벳이 단어 내에 존재할 경우 blind를 해제
        # 존재하지 않을 경우 "없음" 메시지를 출력
     
            

# 게임 종료