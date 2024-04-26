# for count in range(0, 5):
#     print(count)
    

# for문은 반복의 횟수가 명확하게 정해져 있다.
# range에 정확한 범위를 적어놓았다.
    
    
# while 조건식 :
#     pass

# count_w = 0

# while count_w < 5 :
#     print(count_w)
#     count_w += 1
    
# 유효값 : 1 <= trial_num <= 100
# 유효범위 이외 값인 경우 에러메시지 출력 후 재입력

# 무한루프
while True:
    # N값 입력
    trial_num = int(input("N값 : "))
    # 입력받은 N값이 유효범위에 있다면,
    if 1 <= trial_num <= 100 :
        # 무한루프 탈출
        break
    # 함수가 break를 만나면 flow control로 인해 첫 번째 만나는 반복문까지 위로 올라간다. 
    # 반복문을 부순다.그리고 34번 line으로 간다
    
    # if조건식에 만족하지 못한다면(유효하지 않은 값이 들어오면)
    print("에러: 1이상 100이하 값 입력")
import random
# 중복 값이 없는 정수의 개수

# 중복 값이 없는 정수를 저장할 list
made_list = [] 

# trail_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장
for trail_count in range(0, trial_num) :
    
    # 중복 값 검사를 위해서 반복
    while True:
       random_num = random.randint(1, 5)
       
       found_duplication = False
       
       for made_inedx in range(0, trail_count):
           # 중복 값이 있으면
           if made_list[made_inedx] == random_num:
               found_duplication = True
               break
           
       if not found_duplication:
        made_list.append(random_num)
        break
print(made_list)    

while True:
    input_index = int(input("인덱스 : "))
    
    if 0 <= input_index < len(made_list):
        print("원소 값 : ", made_list[input_index])
        break
    print("out of index")

# for n in range(0, 5):
    
#     if n == 1:
#         break 
#     # 함수가 break를 만나면 flow control로 인해 첫 번째로 만나는 반복문까지 위로 올라간다. 
#     # 그리고 반복문을 부순다.그리고 36번 line으로 간다
#     # 특정 조건에서 반복을 멈추고 싶을 때 사용된다.
    
#     print(n)