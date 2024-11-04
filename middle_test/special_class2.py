# 1 이상 30 이하의 정수 중에, 짝수이면서, 5의 배수를 출력하시오


# 내가 짠 것
# for i in range(1, 31) :
#     if i % 2 == 0 and i % 5 == 0 :
#         print(i, "\t" ,end="")

# 교수님이 짜신 것      
# for count in range(1, 31):
#     if count % 2 == 0 and count % 5 == 0 :
#         print(count, "\t", end="")

# and 연산자

# 입력 값이 홀수이면서 3의 배수 값이면 출력하시오.

# input_value = int(input("정수 값 입력: "))

# if input_value % 2 == 1 :
#     if input_value % 3 == 0 :
#         print(input_value)
        
# if input_value % 2 == 1 and input_value % 3 == 0 :
#     print(input_value)

# or 연산자

# 정수를 입력 받아, 입력받은 정수를 화면에 출력하라. <- 무한반복
# 언제까지? 3의 배수 또는 4의 배수가 입력되면, 프로그램을 종료하시오.

# 내가 짠 것
# while True:
#     inputValue = int(input("정수를 입력하세요: "))
#     if inputValue % 3 == 0 or inputValue % 4 == 0 :
#         print(inputValue)
#         break

# # 교수님이 짜신 것
# while True:
#     input_value = int(input("정수값 입력: "))
    
#     if input_value % 3 == 0 or input_value % 4 == 0 :
#         break
    
#     print(input_value)

# for count in range(1, 10):
#     print(count % 5, "\t", end="")
#     # 1       2       3       4       0       1       2       3       4 


# 셋 다 나누기 연산자 이지만,
# 세 개의 출력 값이 다 다르다.

# print(5/2)  # 몫 + 나머지 = 2.5
# print(5//2) # 몫 = 2
# print(5%2)  # 나머지 = 1


# 문자열을 입력 받아, 입력받은 문자열의 길이를 반환하는 함수이다.


# foo 변수에 저장된 문자열의 길이를 출력하시오
foo = 'hello'

count = 0
for value in foo:
    count += 1
    
print(count)
