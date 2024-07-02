# 문제 1 : 키보드로부터 정수 5개를 입력받아 합계와 평균을 출력하는 프로그램을 작성하시오.

# 구현 내용:
# 입력: 사용자로부터 정수 5개를 입력받는다.

# # num1 ~ 5라는 변수를 이용해 사용자로부터 정수를 입력받는다.
num1 = int(input("1번째 값을 입력하세요: "))
num2 = int(input("2번째 값을 입력하세요: "))
num3 = int(input("3번째 값을 입력하세요: "))
num4 = int(input("4번째 값을 입력하세요: "))
num5 = int(input("5번째 값을 입력하세요: "))

# 합계 계산: 입력받은 정수의 합계를 계산한다.
# plus라는 변수를 사용하여 num1 ~ 5의 정수 값을 모두 더한다.
plus = num1 + num2 + num3 + num4 + num5

# 평균 계산: 입력받은 정수의 평균을 계산한다.
# division 이라는 변수를 사용해 사용자로부터 입력받은 정수 값의 합을 5로 나눈다.
division = plus / 5

# 결과 출력: 계산된 합계와 평균을 출력한다.
# 합계는 plus_result,  평균값은 average 라는 변수를 출력한다.
plus_result = print("합계: ", plus)
average = print("평균: ", division)

