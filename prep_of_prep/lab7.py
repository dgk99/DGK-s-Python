# 사칙연산 계산기
# 사용자로부터 두 개의 정수 숫자를 입력 받고, 그 합, 차, 곱, 나눗셈의 결과를 출력하시오

# 사용자에게 두 정수를 입력받습니다.
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
# 입력받은 숫자들의 합, 차, 곱, 나눗셈 결과를 확인
p = float(num1 + num2)
m = float(num1 - num2)
multi = float(num1 * num2)
div = float(num1 / num2)
# 계산된 결과를 출력
print("합: ",p)
print("차: ",m)
print("곱: ",multi)
print("나눗셈: ",div)
