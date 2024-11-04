# 두 수 비교하기
# 첫 줄에 a와 b가 주어진다. a와 b는 공백 한 칸으로 구분되어져 있다.
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
# a가 b보다 큰 경우 > 출력
# a가 b보다 작은 경우 < 출력
# a와 b가 같은 경우 == 출력

num = input()
num = list(map(int, num.split()))

if num[0] > num[1]:
    print(">")
elif num[0] < num[1]:
    print("<")
else:
    print("==")