# 1부터 20까지의 정수 중 짝수의 합계 계산

# continue문 연습
# for문과 continue문을 사용하여 1부터 20까지의 숫자 중 홀수를 건너뛰고 짝수의 합계를 계산

sum = 0

for i in range(1, 21) :
    if i % 2 != 0 :
        continue
    else:
        sum += i
        
print("1부터 20까지의 짝수 합계 (홀수 건너뜀):",sum)