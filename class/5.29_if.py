# value = 3

# # 2 + 3 => 5
# # if 5 : <- 5를 boolean형으로 변환한다.
# # 데이터 타입이 boolean형이 아닌걸 불린형으로 취급할 수 있는걸 truthy falsy 이다.
# # 0일때만 false 0이 아닌 수는 true
# if 2 + 3 :
#     print("a")
#     print("b")
#     print("c")
    
# # 이 식은 5 - 5 => 0이니까 falsy로 인해 d가 출력된다.
# if 5 - 5 :
#     print("a")
#     print("b")
#     print("c")

# print("d")

# color = input("색을 적으세요: ")
# car = ""
# # 색깔이 빨강이면 포드
# if color == "빨강" :
#     car = "포드"
# # 색깔이 회색이면 벤틀리
# elif color == "회색" :
#     car = "벤틀리"
# # 색깔이 검정이면 현대
# elif color == "검정" :
#     car = "현대"
# # 빨,회,검정색이 아니면 벤틀리 출력
# else:
#     car = "벤틀리"

# # 색깔이 빨강이면 포드
# if color == "빨강" :
#     car = "포드"
# # 색깔이 회색이면 벤틀리
# elif color == "회색" :
#     car = "벤틀리"
# # 색깔이 검정,파랑이면 현대
# elif color == "검정" or color == "파랑" :
#     car = "현대"


# print(car)

# model = input("자동차 모델을 입력하세요: ")
# maker = "알 수 없는 모델입니다."

# list_BMW = ["M1","M2","M3","M4","M5","M6","M7","M8","M9"]
# list_Tesla = ["Y", "X"]
# list_Lexus = ["ES", "LS"]
# list_Hyundai = ["G80", "G90"]

# if model in list_BMW :
#     maker = "BMW"
# elif model in list_Tesla :
#     maker = "Tesla"
# elif model in list_Lexus :
#     maker = "Lexus"
# elif model in list_Hyundai :
#     maker = "Hyundai"
# print(maker)

# model = input("자동차 모델을 입력하세요: ")
# # maker = "알 수 없는 모델입니다."
# maker = ""

# list_BMW = ["M1","M2","M3","M4","M5","M6","M7","M8","M9"]
# list_Tesla = ["Y", "X"]
# list_Lexus = ["ES", "LS"]
# list_Hyundai = ["G80", "G90"]

# for b in list_BMW :
#     if model == b :
#         maker = "BMW"
#         break
# if maker == "":
#     for t in list_Tesla :
#         if model == t :
#             maker = "Tesla"
#             break
# if maker == "":
#     for l in list_Lexus :
#         if model == l :
#             maker = "Lexus"
#             break
# if maker == "":
#     for h in list_Hyundai :
#         if model == h :
#             maker = "Hyundai"
#             break

# maker = maker if maker != "" else "알 수 없는 모델입니다"    

# print(maker)

# # M3, M5, M7 = BMW
# if model == "M3" or model == "M7" or model == "M7" :
#     maker = "BMW"
# # Y, X = Tesla
# elif model == "X" or model == "Y" :
#     maker = "Tesla"
# # ES, LS = Lexus
# elif model == "ES" or model == "LS" :
#     maker = "Lexus"
# # G80, G90 = Hyundai
# elif model == "G80" or model == "G90" :
#     maker = "Hyundai"
# # 이외 모델 = 알 수 없는 모델입니다.
# else:
#     maker = "알 수 없는 모델입니다."
    

# test = ["a", "b", "c", "d"]

# print("a" in test) # True
# print("b" in test) # True
# print("c" in test) # True
# print("d" in test) # True
# print("e" in test) # False



model = input("자동차 모델을 입력하세요: ")

list_BMW = ["M1","M2","M3","M4","M5","M6","M7","M8","M9"]
list_Tesla = ["Y", "X"]
list_Lexus = ["ES", "LS"]
list_Hyundai = ["G80", "G90"]

list_model = [list_BMW, list_Tesla, list_Lexus, list_Hyundai]

maker_name_list = ["BMW", "Tesla", "Lexus", "Hyundai"]
index_count = 0

# 회사 목록을 가지고 온다. : 반복 -> 4회 -> bmw, tesla, lexus, hyundai
# 세로 반복
for maker_list in list_model :
    # 회사별 자동차 모델을 가지고 온다. -> 반복 횟수는? 회사별 모델 횟수에 따라 다름
    # 가로 반복
    for model_in_list in maker_list :
        if model == model_in_list :
            maker = maker_name_list[index_count]
            break
    
    if maker != "":
        break
           
    index_count += 1

maker = ""