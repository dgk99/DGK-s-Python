# # while

# # while 조건식 :
#     # 참 일때 실행되는 문장
    
# # 키보드로부터 정수를 입력 받고, 양수일 경우 출력
# # 음수 또는 0인 경우 재입력 -> 양수가 입력 될 때 까지
# while True :
#     user = int(input("정수 입력 : "))
#     if user > 0 :
#         print(user)
#         break

# while문을 이용하여 1에서 10까지 출력하는 프로그램을 작성

# num = 1
# while True :
#     print(num)
#     num += 1
#     if num == 11 :
#         break
    
# while num <= 10 :
#     print(num)
#     num += 1 # 증감식을 missing하는 경우가 있다!! 주의

bar = ["hello", "world", "Richard"]
# found_word = False # flag 변수 -> 깃발 : Boolean

for word in bar :
    
    if word == "world" :
        print("단어를 찾았음")
        # found_word = True
        break
    
else: # 이 else는 반복문이 정상적으로 종료될 때만 선택하고,
    # break를 사용하여 비정상적으로 반복을 마치면 선택되지 않는다
    # ㄴ> 이 else를 사용하면 flag 변수를 만들 필요가 없다
    # 정상적으로 반복을 마쳤을 때 실행된다
    # 반복문이 종료되는 경우는 2가지
    # 1. 반복의 횟수가 완료될 때
    # 2. break와 retrun
    print("단어를 찾지 못했음")
    
# if not found_word :
    