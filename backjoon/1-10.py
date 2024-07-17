# 곱셈

num1 = int(input("첫째 줄에 들어갈 세 자리 수: "))
num2 = (input("둘째 줄에 들어갈 세 자리 수: "))

result6 = num1 * int(num2)
num2 = list(num2)
result3 = int(num2[2]) * num1
result4 = int(num2[1]) * num1
result5 = int(num2[0]) * num1

print(f"{result3}\n{result4}\n{result5}\n{result6}")