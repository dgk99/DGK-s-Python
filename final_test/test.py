# b_count = 2
# n_count = 1
# for i in range(3):
#     for b in range(b_count):
#         print("a",end="")
#     b_count -= 1
#     for n in range(n_count):
#         print("*",end="")
#     n_count += 1
#     print()

# import random


# num_list = [int(value) for value in range(0, 10)]
# print(num_list)
# for _ in range(4):
#     del num_list[random.randint(0, len(num_list) - 1)]
# print(num_list)

dan_input = "2"

input_list = []
for i in dan_input:
    if i == "~":
        del dan_input[i]
    input_list.append(int(i))
print(input_list)
