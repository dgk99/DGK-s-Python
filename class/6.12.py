# argument

# 1) positional argument

# def foo(arg_a, arg_b, arg_c): # foo함수의 매개변수는 3개
#     print(arg_a, arg_b, arg_c)
    
# foo(1, 2) # foo함수에 넣을 인자값은 2개 -> result : error
# 매개변수와 인자값의 갯수는 항상 동일해야 한다

# 함수를 호출할 때, 인자값들을 매개변수에 넣어준다.
# 이 때, 1은 arg_a, 2는 arg_b, 3은 arg_c에 들어간다.
# 위치 기반으로 인자값이 들어간다.
# 첫 번째 인자값은 첫 번째 매개변수
# 두 번째 인자값은 두 번째 매개변수
# 세 번째 인자값은 세 번째 매개변수
# 이 당연하게 여긴 것들을 positonal argument 라고 정의한다.

# 2) keyword argument
# def pos(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)

# pos(arg_c = 1, arg_a = 2, arg_b = 3) # result = 2 3 1
# keyword argument는 순서가 의미 없다.
# 매개변수의 이름을 이용해서 지정한다.
# 이러면 매개 변수의 이름을 다 알아야하고 값을 다 넣어야 하니 불편하다
# 그런데도 왜 이런 불편한 keyword argument를 만들었을까?
# ㄴ>

# 3) default argument
# def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
#     print(arg_a, arg_b, arg_c, arg_d)

# kin()                   # result = 1 2 3 4
# kin(6, 7, 8, 9)         # result = 6 7 8 9
# kin(6)                  # result = 6 2 3 4
# kin(6, 7)               # result = 6 7 3 4
# kin(6, 7, arg_d = 10)   # result = 6 7 3 10


# 구구단을 출력하는 프로그램을 작성 : 2단에서 9단
# 함수로 작성 
# printMulTable(2, 3) -> 2단과 3단을 출력
# printMulTable(3) -> 3단만 출력
# for dan in range(2, 10):
#     for num in range(1, 10):
#         print(f"{dan} X {num} = {dan * num}")
#     print()

# def printMulTable(arg_start, arg_end = None):
    
#         # 인자 값이 한 개가 입력 되었을 경우
#         # arg _start 값만 출력한다.
#         # range(arg_start, arg_end + 1)
        
#         # if arg_end == None:
#         #     arg_end = arg_start
        
#         arg_end = arg_start + 1 if arg_end is None else arg_end + 1
#         for dan in range(arg_start, arg_end):
#             for num in range(1, 10):
#                 print(f"{dan} X {num} = {dan * num}")
#             print()



# def printMulTable(start, end = None):
#     if end == None:
#         end = start
#         for i in range(start, end + 1):
#             for j in range(1, 10):
#                 print(f"{i} X {j} = {i * j}")
#             print()
#     else:
#         for i in range(start, end + 1):
#             for j in range(1, 10):
#                 print(f"{i} X {j} = {i * j}")
#             print()

# printMulTable(2)


# def printMulTable(dan1 = 3, dan2 = 4):
#     if dan1 != 3:
#         for i in range(dan1, dan2 + 1):
#             for j in range(1, 10):
#                 print(f"{i} X {j} = {i * j}")
#     elif dan1 == 3:
#         for i in range(dan1, dan2):
#             for j in range(1, 10):
#                 print(f"{i} X {j} = {i * j}")
        
    
    
# printMulTable(2)

# variable parameter
#     * -> 가변 :  tuple로 받겠다.
# def foo(*args):
#     print(len(args))
#     for value in args:
#         print(value)

# variable parameter
#     * -> 가변 :  Dictionary로 받겠다.
#                 key : value
# def foo(**args):
#     print(len(args))
    
#     for key, value in args.items():
#         print(f"key : {key}, value : {value}")

# foo(test = 2, king = 3)
# foo(test = 2, king = 3, lion = 4)



# def bar(*args):
#     if len(args) == 1:
#         # arg[0]의 값 -> end -> start
#         # chaning
#         start = end = args[0]
        
#     elif len(args) == 2:
#         start , end = args
#     else:
#         return
    
#     for dan in range(start, end + 1):
#         for num in range(1, 10):
#             print(f"{dan} X {num} = {dan * num}")
            
# bar(2)

