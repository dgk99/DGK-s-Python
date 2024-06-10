# import random


# def get_sum():
#     input_value_1 = int(input("입력 값 : "))
#     input_value_2 = int(input("입력 값 : "))
#     input_value_3 = int(input("입력 값 : "))

#     sum = input_value_1 + input_value_2 + input_value_3

#     print(sum)
    
# get_sum()

# random.randint(1,3) # 1이상 3이하의 정수 중에서 난수 하나를 선택해서 반환

# # 파이썬에서 함수를 정의하는 방법
# def 함수명(인자값):
#     함수 호출 시 실행 명령어
    
# # 함수 정의 -> 1번
# def print_name(name):
#     print(name,"님 안녕하세요")
    
# # 함수 호출 -> 2번
# print_name("민규 킴")

# 정수 3개를 입력받아 합계와 평균을 출력하는 프로그램을 작성하라
# 내가 짠 거
# def sum_avg():
#     sum = 0
#     for _ in range(3):
#         sum += int(input("정수를 입력하세요: "))
#     avg = sum / 3
    
#     print(f"합계: {sum}, 평균: {avg}")

# sum_avg()


# 교수님이 짜신 거
# def get_int(arg_num):
#     input_values = []
#     for _ in range(arg_num):
#         input_values.append(int(input("입력값: ")))
        
#     return input_values
# def get_sum_avg(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     avg = sum / len(arg_list)
    
#     return sum, avg
# def get_sum(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
#     return sum

# input_list = get_int(3)

# sum, avg = get_sum_avg(input_list)

# print(avg, sum)

# def sum (arg_first, arg_second):
#     sum = arg_first + arg_second
    
#     if sum < 0:
#         print("음수")
#         return # 반환 값을 꼭 넣어줄 필요는 없다 (break와 유사)
    
#     return sum # 두 가지 역할 -> 1. 함수 종료 2. 값 반환

# result = sum(2, 3)
# print(result) # result => 5

# result = sum(-2, -3)
# print(result)

# 한 개의 정수를 키보드로부터 입력 받아 "짝수", "홀수"를 판별하여 화면에 출력
# 함수로 작성
# def num(user_input):
#     if user_input % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
# user_input = num(int(input("정수를 입력하세요: ")))

# 함수에 인자 값 4개를 입력 받아 합계와 평균을 반환하는 함수를 작성하라
# 그리고 반환된 합계와 평균을 화면에 출력하라.
# def sum_avg(arg_1, arg_2, arg_3, arg_4):
#     sum = arg_1 + arg_2 + arg_3 + arg_4
#     avg = sum / 4
    
#     return sum, avg # 반환 값이 2개 이상이면 tuple로 변환 후 반환한다

# arg_1, arg_2, arg_3, arg_4 = 1, 2, 3, 4

# print(sum_avg(arg_1, arg_2, arg_3, arg_4))


# def get_sum_avg(argA, argB, argC, argD):
#     sum = argA + argB + argC + argD
    
#     avg = sum / 4
    
#     return sum, avg

# sum, avg = get_sum_avg(1, 2, 3, 4)
# print(sum, avg)

# value = get_sum_avg(1, 2, 3, 4)
# print(value[0], value[1])


# Call-by-value, Call-by-reference

# bar = 3

# def foo(bar):
#     bar = bar + 1
#     print("1:", bar)
    
# foo(bar)
# print("2:", bar)

