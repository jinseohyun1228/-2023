x1_list = [int(i) for i in input().split(" ")]
x2_list = [int(i) for i in input().split(" ")]

y_list = []
for i in x2_list:
    if i < x1_list[1] :
        y_list.append(i)

print(*y_list)
