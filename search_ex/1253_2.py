
from bisect import bisect_left


def binary_search(a_list,n):
    index = bisect_left(a_list,n)
    if index < len(a_list) :
        if a_list[index] == n :
            return 1
    return 0

x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()

t_list =[]

for i in range(len(a_list)):
    for j in range(len(a_list)):
        if i != j:
            t_list.append(a_list[i]+a_list[j])


t_list.sort()

print(t_list)

y = 0
for i in a_list:
    y += binary_search(t_list,i)

print(y)