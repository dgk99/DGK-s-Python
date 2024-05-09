# plus = 3 + 5

# minus = 10 - 4.7

# multiple = 3.3 * 8.6

# division = 5 / 3

# print(plus, minus, multiple, division)

# print(type(plus), type(minus), type(multiple), type(division))

# num1 = 10//3
# num2 = 10/3

# print(num1, num2)

# for divisor in range(6):
#     print(divisor%3)
    
# count = 1

# for dan in range(2, 10):
#     for num in range(1, 10):
#         print(dan, "X", num, "=", (dan*num))
        
#     if count % 3 == 0 :
#         print("=" * 10)
        
#     count += 1
    
# result = 2**3

# print(result)

# for value in range(11):
#     print(2**value)
    
    
# print(3 / 2) # 1.5
# print(3 % 2) # 1
# print(3 // 2) # 1

# print(2**3) # 2^3 => 2*2*2

# # 묵시적 형변환
# print(type(2 + 3.0)) # 2 + 3.0 -> float(2) + 3.0

# # 이항 연산을 할 때, 이 문제가 발생된다.
# # 이 연산을 하려면, 좌항과 우항의 자료형을 일치시켜야 한다.
# # 2 + 3.0
# # int + float -> float
# # float (int -> float) 형을 변환한다. Type conversion(형변환)

# input_srt = input("정수를 입력하세요")

#                            # 명시적 형변환
# input_int = int(input_srt) # input_str: str -> integer by using int() function

# for value in range(1, 11):
#     print(value + "번째 값")
# 이 코드가 오류가 나는 이유는?
# value의 자료형은 int, "번째 값"의 자료형은 str이다.
# 그러므로 int + str은 이루어질 수 없기에 error가 일어난다.
# 그래서 이 코드를 원하는대로 출력하려면, value값을 str로 바꿔주어야 한다.
# 명시적 형변환으로 인해 str(value)로 바꿔주면 1번째 값, 2번째 값...인 원하는 값이 출력된다.


# bar = (2.0 + 3) * 4

# 2.0 + 3 -> 2.0 + float(3)
# 5.0 * 4 -> 5.0 * float(4)
# 20.0