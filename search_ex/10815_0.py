
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

x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()

x2 = int(input())
input_list = input()
t_list = [int(i) for i in input_list.split(" ")]



y_list = []
for i in t_list:
    y_list.append(binary_search(a_list,i))

y_str = ' '.join(str(i) for i in y_list)

print(y_str)


