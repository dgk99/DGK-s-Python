# bar, foo, kin = 10, 20

# print(f"{bar}, {foo}, {kin}")

# def getValue():
#     return 2, 3, 4, 5

# bar, foo, pos, kin = getValue()

# print(getValue())
# # 2, 3, 4, 5
# print(type(getValue()))
# # class 'tuple'

# bar = [2, 3, 4, 5]
# foo = (6, 7, 8, 9) # ( ) <- tuple
# kin = 20, 30, 40, 50 # <- tuple

# print(bar[0])
# print(foo[0eo])

# bar[0] = 20
# # bar[0] = 20
# foo[0] = 60
# # error -> immutable하기 때문

# bar = [9, 4, 5, 7] # 9, 4, 5, 7 -> List로 packing

# seo, foo, pos, kin = bar

# print(f"{seo}, {foo}, {pos}, {kin}")
# # 9, 4, 5, 7


# bar = "hello"

# for char in bar:
#     print(char, end = "")
    
# print()
    
# for char in (foo := "world"):
#     print(char, end = "")

# def getCalcValues(argA, argB):
#     # argA와 argBdml +, -, *, / 값을 반환하는 함수 작성
#     # 값 반환 시 tuple 자료형으로
    
#     # return argA + argB , argA - argB , argA * argB , argA / argB
    
#     sum = argA + argB
#     substract = argA - argB
#     multiply = argA * argB
#     division = argA / argB
#     return sum, substract, multiply, division
    
# sum, substract, multiply, division = getCalcValues(2, 3)

# print(f"{sum}, {substract}, {multiply}, {division}")

# def getCalcValues(argA, argB):
#     # argA와 argBdml +, -, *, / 값을 반환하는 함수 작성
#     # 값 반환 시 tuple 자료형으로
    
#     return argA + argB , argA - argB , argA * argB , argA / argB

# kin = getCalcValues(2,3)

# foo = list(kin)
# foo[0] = foo[0] + 1
# print(foo[0])

# Membership operator
# in, not in
# a in b
# a 값, b sequential object

# def myInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return True
    
#     return False
         
        
# def myNotInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return False
        
#     return True


# bar = [3, 4, 5, 6]

# print(4 in bar)
# print(4 not in bar)

# print(myInOperator(3, [2, 3, 4]))

# print(myNotInOperator(3, [2, 3, 4]))


# Identity Operator
# is, is not

# bar = [2, 3, 4]

# foo = [2, 3, 4]

# pos = bar

# if bar == foo : # result -> 참
#     print("참")
# else:
#     print("거짓")
    
# if bar is foo : # result -> 거짓
#     print("참")
# else:
#     print("거짓")
    
# if bar is pos:
#     print("참")
# else:
#     print("거짓")

# bar = 2
# foo = 2

# if bar is foo:
#     print("참")
# else:
#     print("거짓")