# 1차원 리스트

# bar = [10, 20, 30, 40]

# for item in bar:
#     print(item)
    
# print("-" * 30)

# for index in range(-1, -5, -1):
#     print(bar[index])

# # 원소(Element) 30을 100으로 변경
# # bar[좌표] = 100
# bar[2] = 100

# bar = [0, 0, 0, 0, 0, 0]

# bar = [ 0 for _ in range(6)]

# bar = [0] * 6

# print(bar)

# # 
# # 리스트의 가장 뒤에 추가
# bar.append(100)
# # 리스트 사이에 원하는 좌표에 값 추가
# bar.insert(2, 70)

# print(bar)

# 리스트 안의 모든 원소가 사라질 때 까지 반복
# while len(bar) > 0:
#     # 리스트 안에서 제일 왼쪽의 원소를 빼낸다
#     item = bar.pop(0)
#     print(item)
# 원소가 삭제되면 삭제된 원소의 오른쪽 값이 당겨진다.

# 삭제할 때 마다 원소의 갯수가 줄어든다
# 좌표(index번호)를 가지고 삭제한다.

# del bar[2] # 원소를 삭제하고 끝
# print(bar.pop(2)) # 해당 index의 값을 가져올 수 있다.

# -----------------



