def insertion_sort(a_list):
    left = 0
    for right in range(1,len(a_list)):
        print(right)
        left = right-1
        while a_list[right] < a_list[right] and right > 0:
            a_list[right],a_list[left] = a_list[left],a_list[right]
            right -= 1
            left -= 1
    return a_list

a_list = [4,1,6,8,3,9]
insertion_sort(a_list)
print(a_list)