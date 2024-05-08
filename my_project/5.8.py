# value = int(input("정수 입력: "))

# if value == 3 :
#     print("참")
# else:
#     print("거짓")
    
# if value != 3 :
#     print("참")
# else:
#     print("거짓")
    
# if value > 3 :
#     print("참")
# else:
#     print("거짓")
    
# if value >= 3 :
#     print("참")
# else:
#     print("거짓")
    
# if value < 3 :
#     print("참")
# else:
#     print("거짓")
    
# if value <= 3 :
#     print("참")
# else:
#     print("거짓")
    
    
# 1 < value <= 3 -> c > 1 and c <= 3

# print(2 > 3 < 4)

# value = 4

# if value % 2 == 0 and value % 3 == 0 :
#     print("참")
# else:
#     print("거짓")

# value = 4

# if not value : 
# # if not bool(value):
# # if not bool(4) -> True(0이 아닌 수는 true이기 때문):
# # if not True -> False
#     print("참")
# else:
#     print("거짓")

def bar(argValue):
    print("Bar is invoked")
    return argValue

if True or bar(2) == 2:
    print("참")
else:
    print("거짓")
