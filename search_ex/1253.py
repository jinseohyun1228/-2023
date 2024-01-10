def binary_search(a_list,n):
    r = 0
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return 1
        elif a_list[mid] < n:
            first = mid + 1
        else:
            last = mid - 1
    return 0

def make_list(a_list):
    t_list = []
    for i in range(len(a_list)-1):
        for j in range(i+1,len(a_list)):
            t_list.append(a_list[i]+a_list[j])
    return t_list


x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()

t_list = []
# print(t_list)
y = 0
for i in a_list:
    t_list = a_list[:i] + a_list[i+1:]
    t_list = make_list(t_list)
    y += binary_search(t_list,i)

print(y)