
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

y = 0
b = []
for i in range(len(a_list)):
    temp = a_list[:i] + a_list[i+1:]
    for j in range(len(temp)-1):
        for k in range(j+1,len(temp)):
            if a_list[i] == temp[j] + temp[k]:
                y += 1
                break
print(y)