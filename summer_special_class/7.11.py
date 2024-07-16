# 자료 구조

# bar = [10, 20] # List 생성 [ ]

# foo = (30, 40) # Tuple 생성 ( )

# print(bar[0], foo[0]) # 10, 30

# bar[0] = 100 # Mutable
# foo[0] = 200 # Immutable

# bar = []

# for _ in range(5):
#     bar.append(input("값: "))
    
# print(bar) # 내가 입력한 순서대로 data를 저장
    
# foo = set() # set의 내부 알고리즘에 의하여 순서가 바뀌어 저장됨
# 집합(중복 값이 있을 수 없다. 중복 값을 넣으면 값이 들어가지 않는다.)

# for _ in range(5):
#     foo.add(input("값: "))
    
# print(foo) 

# bar = []

# for _ in range(5):
#     bar.insert(0, input("값: ")) # 내가 삽입하고 싶은 자리에 값을 추가
    
# print(bar)

# import random


# bar = [ random.randint(1, 15) for _ in range(10)]
# print(bar)

# foo = set()

# for index in range(10):
#     foo.add(bar[index])

# print(foo)

# bar = {} # Dictionary를 의미

# print(type(bar))

# bar['DGK'] = "김민규" # key값으로 DGK를 삽입 value값은 김민규

# print(bar['DGK'])

# print(bar['test']

# -----------------------------------------------------------
# 생성(Creation)
# 리터럴(Literal) 사용
# my_dict = {'name' : 'Alice', 'age' : 25}
# print(my_dict)
# # 키워드 인자 사용
# my_dict1 = dict(name='Alice', age=25, country='USA')
# print(my_dict1)
# # 튜플 리스트 사용
# pairs = [("name", "Alice"), ("age", 25), ("country", "USA")]
# my_dict2 = dict(pairs)
# print(my_dict2)
# # 키 리스트와 zip 사용
# keys = ["name", "age", "country"]
# values = ["Alice", 25, "USA"]
# my_dict3 = dict(zip(keys, values)) # zip()을 사용하면 값을 합칠 수 있다.
# print(my_dict3)

# Read, Update, Delete
# 생성
# 연락처 정보를 저장하는 dictionary 생성
# 각 key는 연락처의 속성을 나타내고, 각 값은 해당 속성의 data
# contact = {
#     "name" : "John Doe",
#     "email" : "John.com",
#     "phone" : "123 456 789"
# }
# print(contact)
# # Read
# print("Name:", contact["name"])
# print("Email:", contact["email"])
# print("Phone:", contact["phone"])
# # Update
# contact["email"] = "new.email"
# contact["phone"] = "123 123 123"
# contact["address"] = "daegu donggu"
# print("\nUpdated: ", contact)
# # Delete
# del contact["phone"]
# print("\nDeleted phone:", contact)
# # clear
# contact.clear()

# # Iteration(순회)
# # dictionary 정의
# person = {
#     'name': 'dgk',
#     'age' : 27,
#     'city' : 'daegu'
# }
# # 키 값을 순회
# for key in person:
#     print(f"key: {key}, Value: {person[key]}")
# # item() 메서드를 사용한 순회
# for key, value in person.items():
#     print(f"key: {key}, value: {value}")
# # keys() 메서드를 사용한 순회
# for key in person.keys():
#     print(f'keys: {key}')
# # value() 메서드를 사용한 순회
# for value in person.values():
#     print(f"value: {value}")

# my_dict = dict(name=input())
# print(my_dict)

