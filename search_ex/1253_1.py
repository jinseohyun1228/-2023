x1 = int(input())
input_list = input()
a_list = [int(i) for i in input_list.split(" ")]
a_list.sort()       # 정렬, 중복, 음의 정수, 양의 정수,0

count = 0

for i in range(len(a_list)):
    temp_list = a_list[:i]+a_list[i+1:]
    left = 0
    right = len(temp_list) - 1
    while left < right:
        sum = temp_list[left] + temp_list[right]
        if sum == a_list[i]:
            count += 1
            break
        elif sum < a_list[i]:
            left += 1
        else:
            right -= 1


print(count)