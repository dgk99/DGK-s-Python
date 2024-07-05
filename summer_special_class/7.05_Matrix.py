# 2차원 리스트 7.04

# list comprehension 1
# row = 3
# col = 4
# matrix = [[0 for _ in range(col)] for _ in range(row)]
# # list comprehension 2
# matrix = [[0] * 4 for _ in range(3)]

# bar = [[1, 2, 3, 4], [0, 0, 0, 0], [5, 6, 7, 8]]

# print(bar[1][1])

# bar[1][1] = 100

# print(bar[1][1])

# bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# for col in bar:
#     for item in col:
#         print(item, end=' ')
#     print()

# result_list = []
# count = 0
# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))
# for row_num in range(row):
#     for col_num in range(col):
#         result = input(f"Enter value for {[row_num]}{[col_num]}: ")
#         result_list.append(result_list)
# print(result_list[count])

# ---------------------------------------------------------------------

# 2차원 리스트 7.05
# def print_matirx(arg_list):
#     for row in arg_list:
#         for col in row:
#             print(col, "\t", end="")
#         print()
#     print("-" * 30)

# def del_col(arg_list, col_num):
#     for index in range(len(arg_list)):
#         del matrix[index][col_num]

# matrix = [ [1, 2], [4, 5, 6], [7, 8, 9, 10]]

# print_matirx(matrix)

# del_col(matrix, 1)

# print_matirx(matrix)

matrix = [ [1, 2, 3], [4, 5], [6, 7] ]

# 원소 1개 추가
# matrix[2].append(100)

# 행 1개 추가
# matrix.append([8, 9, 10, 11])

# 리스트 사이에 추가
matrix.insert(2, [100, 200, 300])

print(matrix)

# print(len(matrix))
# print(len(matrix[0]))
# print(len(matrix[1]))
# print(len(matrix[2]))


