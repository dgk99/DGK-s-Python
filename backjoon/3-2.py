test_case = int(input("테스트 케이스: "))

result_list = []

for i in range(test_case):
    num = input(f"{i + 1}번째 입력: ")
    num = list(map(int, num.split(" ")))
    result_list.append(num[0] + num[1])

for _ in result_list:
    print(_)
    

    