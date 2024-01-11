def insertion_sort(a_list):
    index = 1
    while index < len(a_list):
        right = index
        left = right - 1
        err = 0
        while 0 < right and a_list[right] <= a_list[left]:
            if (a_list[right] == a_list[left]):
                a_list = a_list[:right] + a_list[right+1:]
                right -= 1
                err = 1
                break
            else:
                a_list[right],a_list[left] = a_list[left],a_list[right]
            right -= 1
            left -= 1
        index = index + 1 - err
    return a_list

x1 = int(input())

a_list = []
while True :
    try:
        n = int(input())
        a_list.append(n)
    except:
        break

a_list = insertion_sort(a_list)
for i in a_list:
    print(i)
