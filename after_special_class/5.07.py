# n = 5
# # 별을 5개씩 5줄을 출력하는 코드 작성하기
# # 지난 시간에 배운 이중 중첩문 사용

# for i in range(n): # 먼저 세로로 5줄을 출력하는 반복문 작성
#     for i in range(n): # 그 다음 가로로 5개를 출력하는 반복문 작성
#         print("*", end="") # 별을 출력하고, end=""을 사용해 별 옆에 별을 출력
#     print() # print() = enter과 같은 의미기에 5개의 별 출력 후 다음 줄로 넘기는 코드

# 별을 순차적으로 하나씩 늘려나가는 코드
# 가로가 세로 줄 수만큼 증가

# n = 5
# count = 1

# for i in range(n):
#     for i in range(count):
#         print("*", end="")
        
#     print() 
#     count += 1


# n = 5
# count = 5
# for i in range(n):
#     for i in range(count):
#         print("*", end="")
        
#     print()
#     count -= 1
    
    
    
    
# n = 5
# blank_count = 4
# star_count = 1

# for i in range(5):
#     for i in range(blank_count):
#         print(" ", end="")
        
        
#     for i in range(star_count):
#         print("*", end="")
        
        
    
#     print()
#     blank_count -= 1
#     star_count += 1



n = 4
blank_count = n - 1
star_count = 1

for _ in range(n):
    for _ in range(blank_count):
        print(" ", end = "")
        
    for _ in range(star_count):
        print("*", end="")
        
    print()
    blank_count -= 1
    star_count += 2
    