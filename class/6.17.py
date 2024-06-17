# Overloading
# 함수와 메서드에 적용이 된다.
# 사용 목적은? 프로그래머에게 코드 작성의 편리성을 제공하기 위해.
# (Python에선 지원 X)


# def bar(a, b):
#     return a + b

# # bar(2, 3, 4) # error

# def bar(a, b, c):
#     return a + b + c

# def bar(a, b, c, d):
#     return a + b + c + d

# print(bar(2, 3))
# print(bar(2, 3, 4))
# print(bar(2, 3, 4, 5))

# 함수의 이름은 동일하고 매개변수의 갯수에 따라서 적절한 함수를 호출하는 것


# 가변 위치 인자를 이용하면 함수 오버로딩 기능을 구현 할 수 있다.
# def bar(*args):
#     return sum(args)

# print(bar(2, 3, 4, 5))
# print(bar(2, 3, 4))
# print(bar(2, 3))

# def bar(arg_fnc):
#     arg_fnc()
    
# def foo():
#     print("안녕하세요: ")
    
# bar(foo)

# 주민등록번호 문제 함수화 해서 풀기
# 790608-2552416
# 주민번호 입력받기
# user_input = input("주민번호를 입력하세요: ")
# user_input = list(user_input)
# # - 제거
# user_input.remove("-")
# # 곱해야 하는 수 리스트로 만들기
# num_list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# # 주민번호의 앞 12자리를 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5로 곱합니다.
# # • 이 결과를 모두 더합니다.
# sum = 0
# for i in range(12):
#     sum += int(user_input[i]) * num_list[i]
# # • 더한 결과를 11로 나눈 나머지를 구합니다.
# div = sum % 11
# # • 11에서 이 나머지를 뺍니다.
# minus = 11 - div
# # • 결과가 두 자리 숫자일 경우, 10의 자리는 버리고 1의 자리만 사용합니다.
# if minus >= 10:
#     result = minus % 10
# else:
#     result = minus
# # • 최종 결과가 주민번호의 마지막 숫자(검증번호)와 일치하면 유효한 주민번호입니다
# if result == int(user_input[-1]):
#     print("유효한 주민번호 입니다.")
# else:
#     print("유효하지 않은 주민번호 입니다.")
# ---------------------------------------------------------------------------------
# 유효한 주민번호 -> True else False
def get_check_digit(arg_ssid):
    # weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_value = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_value % 11) % 10
    
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크 값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:-1])
    
    if check_digit == int(arg_ssid[-1]):
        return True
    else:
        return False


print(is_valid_ssid("790608-2552416"))