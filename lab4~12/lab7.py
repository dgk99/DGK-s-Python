# 사용자로부터 두 개의 정수 숫자를 입력 받고, 그 합, 차, 곱, 나눗셈의 결과를 출력하는 프로그램을 작성하세요

# 첫 번째 정수를 입력받자
number1 = int(input("첫 번째 숫자를 입력하세요: "))

# 두 번째 정수를 입력받자
number2 = int(input("두 번째 숫자를 입력하세요: "))

# 입력받은 두 숫자의 합을 계산하고 실수로 표현하여 출력한다
sum = float(number1 + number2)
print("합: ", sum)

# 입력받은 두 숫자의 차를 계산하고 실수로 표현하여 출력한다
subtracted = float(number1 - number2)
print("차: ", subtracted)

# 입력받은 두 숫자의 곱을 계산하고 실수로 표현하여 출력한다
multiplied = float(number1 * number2)
print("곱: ", multiplied)

# 입력받은 두 숫자의 나눗셈을 계산하고 실수로 표현하여 출력한다
divided = float(number1 / number2)
print("나눗셈: ", divided)