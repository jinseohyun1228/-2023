x1 = int(input())
x2_list = [int(i) for i in input().split(" ")]

min = x2_list[0]
max = x2_list[-1]

for i in x2_list:
    if i < min:
        min = i
    if i > max:
        max = i

print(min,max)

