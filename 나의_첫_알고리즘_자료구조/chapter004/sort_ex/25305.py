def insertion_sort(s_list):
    for right in range(1,len(a_list)):
        left = right - 1
        while right > 0 and a_list[left] > a_list[right]:
            a_list[left],a_list[right] = a_list[right],a_list[left]
            right -= 1
            left -= 1

def bubble_sort(a_list):
    for i in range(len(a_list)-1):
        for j in range((len(a_list)-1) - i):
            if a_list[j] > a_list[j+1]:
                a_list[j+1],a_list[j]= a_list[j],a_list[j+1]
    return a_list
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



x1,x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)
a_list = [int(i) for i in input().split(" ")]


# insertion_sort(a_list)
# bubble_sort(a_list)
merge_sort(a_list)
print(a_list[-x2])
