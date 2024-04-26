# 정수 세 개를 입력 받아서 제일 큰 값 출력
# 내가 짠 것
# num1 = input()
# num2 = input()
# num3 = input()

# if num1 > num2 and num1 > num3 :
#     print(num1)
# elif num2 > num1 and num2 > num3 :
#     print(num2)
# elif num3 > num2 and num3 > num1 :
#     print(num3)
# elif num1 == num2 == num3 :
#     print("모두 같은 수 입니다.")

# elif num1 == num2 > num3 :
#     print(num1, num2)
# elif num2 == num3 > num1 :
#     print(num2, num3)
# elif num1 == num3 > num2 :
#     print(num1, num3)
    
# 교수님이 짠 것 1번째
# input_1 = int(input("1번"))
# input_2 = int(input("2번"))
# input_3 = int(input("3번"))

# max = input_1

# if max < input_2 :
#     max = input_2
    
# if max < input_3 :
#     max = input_3
    
    
# print(max)

# 교수님이 짜신 두 번째(for문 사용)

# max = -1

# for trial_count in range(1, 4):
#     msg = str(trial_count) + "번"
#     input_value = int(input(msg))
    
#     if max < input_value :
#         max = input_value

    
# print(max)

# 내가 짠 것 변형(모두 같을 때 아무거나 하나 출력)
num1 = input()
num2 = input()
num3 = input()

if num1 >= num2 and num1 >= num3 :
    print(num1)
elif num2 >= num1 and num2 >= num3 :
    print(num2)
elif num3 >= num2 and num3 >= num1 :
    print(num3)

# elif num1 == num2 > num3 :
#     print(num1, num2)
# elif num2 == num3 > num1 :
#     print(num2, num3)
# elif num1 == num3 > num2 :
#     print(num1, num3)