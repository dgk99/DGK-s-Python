# 세 수의 비교 # if, input, print 만 사용

# 세 수 받기
num1 = int(input("첫 번째 수 입력: "))
num2 = int(input("두 번째 수 입력: "))
num3 = int(input("세 번째 수 입력: "))

# 모든 수가 같으면, "모든 수가 같습니다."
if num1 == num2 == num3 :
    print("모든 수가 같습니다.")
# 두 수가 같으면 "두 수가 같습니다." , 같은 두 수도 출력
elif num1 == num2 :
    print("두 수가 같습니다.","(",num1,"와",num2,")")
elif num2 == num3 :
    print("두 수가 같습니다.","(",num2,"와",num3,")")
elif num3 == num1 :
    print("두 수가 같습니다.","(",num3,"와",num1,")")
# 모든 수가 다르면, "모든 수가 다릅니다. 가장 큰 수는 x입니다."
elif num1 != num2 != num3 :
    if num1 > num2 and num1 > num3 :
        print("모든 수가 다릅니다. 가장 큰 수는",num1,"입니다.")
    elif num2 > num1 and num2 > num3 :
        print("모든 수가 다릅니다. 가장 큰 수는",num2,"입니다.")
    elif num3 > num2 and num3 > num1 :
        print("모든 수가 다릅니다. 가장 큰 수는",num3,"입니다.")

