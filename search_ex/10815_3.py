
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

def sort(a_list):
    if len(a_list) <= 1 :
        return a_list
    mid = len(a_list)//2
    left_list = a_list[:mid]
    right_list = a_list[mid:]
    left_list = sort(left_list)
    right_list = sort(right_list)

    a_index = 0
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            a_list[a_index] = left_list[left_index]
            left_index += 1
        else:
            a_list[a_index] = right_list[right_index]
            right_index += 1
        a_index += 1

    while left_index < len(left_list):
        a_list[a_index] = left_list[left_index]
        left_index += 1
        a_index += 1

    while right_index < len(right_list):
        a_list[a_index] = right_list[right_index]
        right_index += 1
        a_index += 1

    return a_list


x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list = sort(a_list)

x2 = int(input())
input_list = input()
t_list = [int(i) for i in input_list.split(" ")]


y_list = []
for i in t_list:
    y_list.append(binary_search(a_list,i))

y_str = ' '.join(str(i) for i in y_list)

print(y_str)


