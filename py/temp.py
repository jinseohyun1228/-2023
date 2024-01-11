n ="\n"
a = "안녕하세여"+n+"d"
b = "인녕하시렵니까?"+n

print(a+b)

total_n = 9
a = [] * total_n
index = 0
n = total_n // 3

b = "+"*total_n
print(b)

for i in range(0, n):
    print(i)

print("------")
for i in range(n, n * 2):
    print(i)
print("------")

for i in range(n * 2, n * 3):
    print(i)

# total_n = 9
# total_list = []
# for i in range(total_n):
#     row = ["3"] * total_n
#     total_list.append(row)
# print(total_list[2][3])
#
#
# for row in total_list:
#     print(row)


"""
n = 3  # n을 원하는 크기로 변경하세요

# n x n 2차원 배열 생성
two_dimensional_array = []
for i in range(n):
    row = [0] * n
    two_dimensional_array.append(row)

# 배열 출력
for row in two_dimensional_array:
    print(row)
"""
#
# total_n = 9
# total_list = []
# n = total_n // 3
# for i in range(total_n):
#     row = [""] * total_n
#     total_list.append(row)
#
# for i in range(0, n):
#     for row in range(total_n):
#         total_list[i][row] = "*"
#     print(total_list[i])
#     print("d")

a_list = [1,3,4,5]
b_list = [3,4]

c = a_list + b_list

print("!!" + str(c[0:6]))

print(c)
i = 5
print(c[:i]+c[i+1:])
