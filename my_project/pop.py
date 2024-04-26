# 교수님 예시
import random
n = 5
max_num = 6

sample_list = [ value for value in range(1, max_num) ]
# sample_list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_list = []

for trial_count in range(0, n):
    random_index = random.randint(0, len(sample_list) - 1)
    random_num = sample_list.pop(random_index)
    random_list.append(random_num)    
    
print(random_list)