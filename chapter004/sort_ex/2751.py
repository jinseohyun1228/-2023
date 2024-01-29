def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list)//2
        left_list = a_list[:mid]
        right_list = a_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        a_index = 0
        left_index = 0
        right_index = 0
        while right_index < len(right_list) and left_index < len(left_list):
            if left_list[left_index] < right_list[right_index]:
                a_list[a_index] = left_list[left_index]
                a_index += 1
                left_index += 1
            else:
                a_list[a_index] = right_list[right_index]
                right_index += 1
                a_index += 1

        while left_index < len(left_list):
            a_list[a_index] = left_list[left_index]
            a_index += 1
            left_index += 1

        while right_index < len(right_list):
            a_list[a_index] = right_list[right_index]
            right_index += 1
            a_index += 1

        return a_list

x1 = int(input())

a_list = []

for i in range(x1):
    a_list.append(int(input()))

merge_sort(a_list)
s = ""

for i in a_list:
    s = s + str(i) +"\n"

print(s)