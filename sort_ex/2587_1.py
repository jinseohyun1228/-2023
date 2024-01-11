a_list = []

for i in range(5):
    a_list.append(int(input()))

a_list.sort()

average = int(sum(a_list)//len(a_list))
mid = a_list[int(len(a_list)//2)]

print(average)
print(mid)