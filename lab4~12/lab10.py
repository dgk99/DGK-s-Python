# 사용자로부터 세 개의 정수 숫자를 입력받고, 이 중 가장 큰 숫자를 찾아 출력하는 프로그램을 작성하시오.
# 첫 번째 숫자를 입력받는다.
num1 = int(input("첫 번째 숫자를 입력하세요: "))

# 두 번째 숫자를 입력받는다.
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 세 번째 숫자를 입력받는다.
num3 = int(input("세 번째 숫자를 입력하세요: "))

# 입력받은 세 숫자 중 첫 번째 숫자가 가장 클 때, 가장 큰 숫자는 num1입니다 라고 출력한다.
if num1 > num2 and num1 > num3:
    print("가장 큰 숫자는",num1,"입니다.")
    
# 입력받은 세 숫자 중 두 번째 숫자가 가장 클 때, 가장 큰 숫자는 num2입니다 라고 출력한다.
if num2 > num1 and num2 > num3:
    print("가장 큰 숫자는",num2,"입니다.")
    
# 입력받은 세 숫자 중 세 번째 숫자가 가장 클 때, 가장 큰 숫자는 num3입니다 라고 출력한다.
if num3 > num1 and num3 > num2:
    print("가장 큰 숫자는",num3,"입니다.")