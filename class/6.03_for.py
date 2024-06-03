
# # 화면에 1을 10번 출력한다 -> 반복을 10번
# for _ in range(10):
#     print(1)
    
# for value in range(10):
#     print(1)
    
    
# for value in range(7, 8) :
#     print(value)

# 증감값이 기본적으로 1이 들어가기에, 이 코드는 아무것도 출력하지 않는다
# for value in range(7, -8) :
#     print(value)
# range를 쓸 때 반복의 횟수가 0이 될 수 있다.

# for value in range(5, 1) : # == range(5, 1, 1)
#     print(value)

# for value in range(5, 1, -2) : # 5, 3, (1(종료값과 같으므로 출력되지 않음))
#     print(value)
    
# for value in range(5, -20, -5) : # 5, 0, -5, -10, -15, (-20(종료값과 같으므로 출력되지 않음))
#     print(value)

# # 단순 반복
# for _ in range(8):
#     print(_, end="")
    
# print("\n", "*" * 20)

# # 시작 값과 끝 값이 코드 내에서 사용될 때
# for dan in range(2, 10):
#     print(dan, end="")

# 1에서 20까지 정수로 구성된 리스트를 생성하세요.
# num_list = []
# for num in range(1, 21):
#     num_list.append(num)
# print(num_list)

# # list comprehension(리스트 컴플리헨션)
# # 리스트 내 원소 값들을 for 문을 사용하여 동적으로(프로그램이 실행하면서 뭔가 변하는 것) 생성
# # [ expression for item in item_list if conditional expression ]
# num_list = [_ for _ in range(1, 21)]
# print(num_list)

# value = int(input("양의 정수를 입력 하세요: "))
# num_list = [value for value in range(1, value)]
# print(num_list)
# # 프로그램이 실행되고 값 들이 결정된다 -> 동적이다   
 
# num_list = list(range(1, 21))
# print(num_list)

# 7로 초기화된 8개의 원소를 가지는 리스트를 생성하라
# seven_list = [ 7 for _ in range(8) ]
# print(seven_list)

# for문의 반복횟수가 무엇을 결정하는가?
# 원소의 갯수
# for문 앞에 있는 수식은
# 원소 값

# 1부터 21까지 숫자를 생성하고, 그 수가 3의 배수일 경우 리스트에 저장
# bar = [value for value in range(1, 21) if value % 3 == 0 ]
# print(bar) # 3, 6, 9, 12, 15, 18

# 아래 리스트 중 'c'가 포함된 단어만 선택해서 리스트로 구성하라
# foo = ["abc", "dcd", "ef", "gh"]
# find_c = [value for value in foo if "c" in value]
# print(find_c)

# s_list = [ word for word in foo if "c" in word ]

# 아래 리스트 중 단어의 글자 갯수가 3개 이상인 단어만 선택하여 리스트로 생성

# foo = ["abc", "dcd", "ef", "gh"]

# three_word = [ value for value in foo if len(value) >= 3]
# print(three_word)

# 1에서 10사이 정수 중, 홀수는 10을 곱하고, 짝수는 20을 곱한 리스트를 생성
# result = [10, 40, 30, 80, 50, 120, 70, 160, 90, 200]

# 힌트 1 range 뒤에 if 없어도 가능
# 힌트 2 삼항연산자(참 if 조건식 else 거짓 -> 수식) 사용
# num_list = [ num * 10 if num % 2 != 0 else num * 20 for num in range(1, 11) ]
# print(num_list)

# s_list = [value for value in range(1, 21) if value % 3 == 0 if value % 4 == 0]

