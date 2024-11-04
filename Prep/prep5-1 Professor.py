#사용자로부터 세 개의 정수를 입력 받는다. ü 세 수의 관계에 따라 다음과 같이 출력한다:
# a, b, c
a = int(input("첫 번째 숫자 입력: "))
b = int(input("두 번째 숫자 입력: "))
c = int(input("세 번째 숫자 입력: "))
#① 모든 수가 같으면, "모든 수가 같습니다."
#조건: a == b and b == c and a == c
if a == b and b == c and a == c :
    print("모든 수가 같습니다.")
#② 두 수가 같으면, 
# 조건: a==b or b==c or c==a
# "두 수가 같습니다."출력.
elif a==b or b==c or c==a :
    print("두 수가 같습니다")
# 와 같은 두 수도 출력. 
# 조건: a==b -> a,b 출력
# 조건: c==b -> c,b 출력
# 조건: a==c -> a,c 출력
    if a==b :
        print(a, ":", b)
    elif b==c :
        print(b, ":", c)
    else:
        print(a, ":", c)
        
    
#③ 모든 수가 다르면, 
# "모든 수가 다릅니다. 
else:
    print("모든수가 다릅니다.")
# 가장 큰 수는 X입니다." 
# X는 가장 큰 수.
# 조건: a > b and a > c -> a가 최대 값
# 조건: b > a and b > c -> b가 최대 값
# 조건: 위 조건을 만족하지 않으면, c가 최대 값.
    if a > b and a > c :
        print(a, "가 최대 값")
    elif b > a and b > c :
        print(b, "가 최대 값")
    else:
        print(c, "가 최대 값")

# 문제를 계속 짜개라.
# 잘하는 사람 껄 봐라.
# 