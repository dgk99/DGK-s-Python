# # is, is not -> Identity operator

# # 메모리 상에 2, 4, 5라는 원소가 저장됐다.
# bar = [2, 4, 5]
# # 2, 4, 5가 위치한 메모리 상의 주소를 알아야 CRUD 할 수 있다.
# # 이 주소값을 저장해야 하는데, 이 원소들의 주소를 다 저장하지 말고,
# # 첫 번째 원소의 주소값만 가지고 있고, 그 뒤의 것들은 인덱스를 이용해 순차적으로 관리하자.
# # 참조 변수 : 메모리 주소값을 저장하기 위한 변수
# # 인덱스가 왜 필요한가? 해당 원소를 찾아가기 위해
# foo = [2, 4, 5]

# if bar == foo :
#     print("참")
#     # 파이썬에선 좌항과 우항에 리스트가 오면, 참조변수가 가리키는 주소값을 비교하는 게 아니라, 원소값이 같은지 틀린지 비교한다.
#     # 파이썬에서 연산자 기능이 재정의 되어있다.
# else:
#     print("거짓")
    
    
    
# if bar is foo :
#     print("참")
# # 변수에 들어가있는 주소값 그 자체를 비교하려면, Identity operator가 필요하다.
# # is 연산자는 이항연산자로써, 좌항에 우항에 참조변수의 주소값 그 자체를 비교한다.
# else:
#     print("거짓")
    
#     # 인덱스가 없으면 리스트 안의 모든 원소의 값을 저장하기 위한 참조 변수가 필요하기에 불편하다.
#     # 그래서 인덱스가 필요하다.
#     # 참조변수는 리스트 안의 모든 변수를 접근해야 하는데, 참조 변수에 첫 번째 참조변수에 리스트의 주소값이 들어가 있다.
    
    

# msg = ""
# value = 1
# if value == 1 :
#     msg = "안녕"
# else:
#     msg = "hello"
    
# # 삼항(Ternary) 연산자
# msg = "안녕" if value == 1 else "hello"
# # 값이 있으면 조건식에 따라서 두 개 중 하나를 선택하는 것
# # if, else문을 사용해도 되지만, 코드의 가독성이 좋지 않다.
# # 삼항 연산자 -> if, else로는 전환이 가능하나,
# # if, else -> 삼항 연산자로는 전환이 가능할 수도 있고 안될 수도 있다.

# strike_out = True

# print("lose" if strike_out else "win")

# if strike_out :
#     print("lose")
# else:
#     print("win")


# 이 자리는 내꺼 ㅎ
#이제 이 자리는 제겁니다 제 마음대로 사고 팔 수 있죠

# 1412
#괴도P
