test_case = int(input())

result_list = []

for i in range(test_case):
    num = list(map(int, input().split(" ")))
    result_list.append(num[0] + num[1])

for _ in result_list:
    print(_)
    

    