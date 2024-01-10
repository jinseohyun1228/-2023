import bisect
from bisect import bisect_left


def binary_search(a_list,n):
    r = 0
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if a_list[mid] == n:
            temp = inverse_linear_search(a_list[first:mid],n)
            temp = mid - temp
            while True :
                if a_list[temp] != n:
                    return r
                temp += 1
                r += 1
        elif a_list[mid] < n:
            first = mid + 1
        else:
            last = mid - 1  # ⭐
    return r

def inverse_linear_search(a_list,n):
    for i in range(len(a_list)):
        if a_list[-(i+1)] != n:
            return i
    return len(a_list)-1



x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()

t_list =[]

for i in range(len(a_list)):
    for j in range(len(a_list)):
        if i != j:
            t_list.append(a_list[i]+a_list[j])

print(t_list)

t_list.sort()

print(t_list)
y = 0
for i in a_list:
    y += binary_search(t_list,i)

print(y)