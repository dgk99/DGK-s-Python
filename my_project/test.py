# a = [10, 100, 20]

# for index in range(0, len(a)): # 0, 3 : len(list) -> 리스트의 원소 갯수
#     print(a[index]) # index 0 -> 2
    
# bar = [value for value in range(10, 20)]

# print(bar)

# # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# # slicing
# # 참조변수 [ start : stop : step ]

# # start : 0 -> stop : 4 - 1
# foo = bar[ 0 : 4 : 1 ]

# print(foo)

# bar = [2, 3, 4, 5, 6]

# bar[0 : 3] = [100, 200, 300]

# print(bar) # [100, 200, 300, 5, 6]

# bar = [10, 20, 30, 40, 50, 60]
# print("before : ", bar, len(bar)) # [10, 20, 30, 40, 50, 60]
# del bar[1] # [10, 30, 40, 50, 60]
# print("after : ", bar, len(bar))

# bar = [10, 50, 30, 40, 50, 60]

# bar.remove(50)
# print("after : ", bar, len(bar))

bar = [10, 20, 30, 40, 50, 60]
# print("before : ", bar, len(bar))

print(bar.pop(2))
print("after : ", bar, len(bar))

# 1 ~ 10 사이 정수 중, 중복되지 않은 정수 N개 선택

# sample_list = [value for value in range(1, 11)]
# import random
# n = 5
# random_list = []

# for trial_count in range(0, n) :
#     random_index = random.randint(0, len(sample_list) - 1)
#     random_num = sample_list.pop[random_index]
#     random_num.append(random_num)
bar = [1, 2, 3, 4, 5]
bar.clear()
print(bar)


foo = [1, 2, 3, 4, 5]
del foo