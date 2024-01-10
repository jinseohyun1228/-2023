


# def linear_serch(a_list,n):
#     if n in a_list:
#         return 1
#     else:
#         return 0
def binary_search(a_list,n):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first+last)//2
        if a_list[mid] == n:
            return 1
        elif a_list[mid] < n:
            first = mid +1
        else:
            last = mid -1
    return 0

from sys import stdin
x1 = int(stdin.readline())
a_list = list(map(int,stdin.readline().split()))
a_list.sort()

x2 = int(stdin.readline())
t_list = list(map(int,stdin.readline().split()))



y_list = []
for i in t_list:
    y_list.append(binary_search(a_list,i))

y_str = ' '.join(str(i) for i in y_list)

print(y_str)


