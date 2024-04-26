num1 = print("첫 번째 값을 입력하세요")
num1_input = input()

num2 = print("두 번째 값을 입력하세요")
num2_input = input()

operator = print("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)")
operator_input = input()



if operator_input == '+' :
    num_result = float(num1_input + num2_input)
elif operator_input == '-' :
    num_result = float(num1_input - num2_input)
elif operator_input == '*' :
    num_result = float(num1_input) * float(num2_input)
elif operator_input == '/' :
    num_result = float(num1_input) / float(num2_input)

datatype = print("결과 값 자료형(integer, flaot, string 중 하나 입력)")
datatype_input = input()

if datatype_input == 'integer':
    num_result = int(num_result)
elif datatype_input == 'float':
    num_result = float(num_result)
elif datatype_input == 'string':
    num_result = str(num_result)

    
result = print("결과 값은 아래와 같습니다.")
result_output = print(f"{num1_input} {operator_input} {num2_input} = {num_result}")

print(type(num_result))