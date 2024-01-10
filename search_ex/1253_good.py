x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()


count = 0

for i in range(len(a_list)):
    left = 0
    right = 0

    while left < len(a_list) and right < len(a_list):
        sum = a_list[left] + a_list[right]
        if sum == a_list[i] :
            if left != right and left != i and right != i:
                count += 1
            left += 1
        elif sum < a_list[i] :
            left += 1
        else:
            right += 1
    while left < len((a_list)):
        sum = a_list[left] + a_list[-1]
        if left != (right-1) and left != i and (right-1) != i:
            count += 1
        left += 1
    while right < len(a_list):
        sum = a_list[-1] + a_list[right]
        if (left-1) != right and (left-1) != i and right != i:
            count += 1
        right += 1
print(count)
