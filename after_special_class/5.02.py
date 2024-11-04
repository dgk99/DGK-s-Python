# 반복문 안에 반복문

# 키보드로 부터 정수를 입력 받고, 입력 받은 정수 개수만큼 *을 출력하세요
# ex) 입력 정수 : 3
# 결과 : ***

# num = int(input("입력 정수 : "))

# print("*" * num)

# 조건 : 연산자 사용 금지 (print("*"*3))

# 반복의 횟수가 num만큼 돌아야 하기에 for 문을 쓰면 된다

# for _ in range(0, num) :
#     print("*", end="")
    
# print를 출력하면 우리가 입력하지 않아도, 문자열 뒤에 \n이 붙는다
# 이걸 안하고 싶다면, end=""를 삽입하면 된다.

# 입력 받은 정수 개수의 가로 * 세로 바둑판 출력
# 결과) 
# ***
# ***
# ***
# num = int(input("입력 정수 : "))

# for i in range(0, num):
    
#     for a in range(0, num):
        
#         print("*", end="")
        
#     print()
    
# 이런 2중 반복문을 쓰는 경우를 Nested(중첩)이라고 한다.

# count = 1

# for _ in range(3):
#     for _ in range(2):
    
#         print(count)
#         count += 1
        
# 이중 for문이 있으면, 안쪽 것 부터 해석 하자
# for _ in range(3):
#     for _ in range(3):
#         print("*", end="")
#     print()
# 첫 번째 for문의 반복이 3번, 두 번째 for문의 반복이 3번 이면, 
# 3 * 3  = 9가 아닌 3개 짜리가 3번 나온다고 해석하자

for _ in range(2):
    for _ in range(4):
        print("*", end="")
        
    print()
    print()
