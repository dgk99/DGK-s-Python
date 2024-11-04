#for value in range(5): # N -> N번 반복, 0 -> N-1, 
                        # 5 -> 5번 반복, 0 -> 4
    
# Q.왜 0부터 시작하는가?
# A.리스트 안을 순회하는데, index값이 0부터 시작하기 때문에



# 반복문이 종료되는 경우
# 1. 조건식을 만족하고 정해진 횟수를 반복했을 경우
# 2. 조건식을 만족하지 못하고 비 정상적으로 멈추는 경우
# done_break = False
# for value in range(3):
#     inputValue = int(input("입력 값: "))
#     if inputValue <= 0:
#         done_break = True
#         break
#     print(value)
    
# msg = "break 사용" if done_break else "break 미사용"

# print(msg)

# 반복을 총 3번 하는데 반복이 3번 다 되었는지 확인하고 싶을 때
# boolean형으로 가지는 flag 변수를 사용한다

# #done_break = False
# for value in range(3):
#     inputValue = int(input("입력 값: "))
#     if inputValue <= 0:
# #        done_break = True
#         msg = "break 사용"
#         break
#     print(value)
# else: # 반복문 종료 and break 미사용
#     msg = "break 미사용"
# # msg = "break 사용" if done_break else "break 미사용"
# print(msg)







# 반복의 횟수를 효율적으로 제어하기 위해

# break - 반복을 중지
# continue - 특정 조건을 유지하면서 반복을 중지하고 싶을 때
# pass (Python)

# for i in range(1, 3): # 1 ~ 2
#     for j in range(1, 4): # 1 ~ 3
#         if i == 2:
#             break
#         print(i, ":", j)
        # 나의 답변 2 : 4 <- 땡!!
        
# 밑에서 위로 해석하면 빨리 이해가 된다
# ㄴ>j가 i번 돈다고 생각하자

# ***별을 4줄 출력하시오(곱하기 연산자 사용 금지)
# for star1 in range(1, 5):
#     print()
#     for star2 in range(1, 4):
#         print("*", end = "")
        
# 가로 for문 먼저 만들고 그 위에다 세로 for문을 얹자
# -> 가로 for문이 세로 for문 만큼 반복
# for i in range(4):
#     for j in range(3):
#         print("*", end = "") # ***
#     if i != 3:
#         print()

# for k in range(1, 5):
#     for i in range(1, 3): # 1 ~ 2
#         for j in range(1, 4): # 1 ~ 3
#             if i == 2:
#                 break
#             print(i, ":", j)
            
# break 동작 절차:
# 1) 위로 올라간다
# 2) 첫 번째 만나는 반복문을 종료한다.

# continue 동작 절차:
# 1) 위로 올라간다
# 2) 다음 반복문을 종료한다.

# 1 1
# 1 2
# 1 3 이 4번
# break가 78번의 for문을 탈출

# for k in range(1, 5):
#     if k == 2:
#         break
#     for i in range(1, 3): # 1 ~ 2
#         for j in range(1, 4): # 1 ~ 3
#             print(i, ":", j)
            
# 1 1 
# 1 2 
# 1 3 
# 2 1 
# 2 2 
# 2 3
# break는 92번을 종료

# for k in range(1, 4):
#     if k == 2:
#         continue
#     for i in range(1, 3): # 1 ~ 2
#         for j in range(1, 4): # 1 ~ 3
#             print(i, ":", j)

# pass : 흐름제어문, 함수, 클래스
# 알고리즘을 구현해야 하는데, 나중에 구현해야 할 때 pass 사용

value = 3

if value > 3:
    # 메뉴를 출력하라 -> 추후 구현해야함
    pass

def sum(a, b, c):
    # 3개의 값을 더한 후 반환
    # 추후 구현
    pass


count = 2