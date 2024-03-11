def insertion_sort(a_list):
    for right in range(1,len(a_list)):
        left = right - 1
        while right < len(a_list) and a_list[right] < a_list[left]:
            a_list[left],a_list[right] = a_list[right],a_list[left]
            right -= 1
            left -= 1
    return a_list

def average(a_list):
    sum = 0
    for i in a_list:
        sum += i
    return sum//len(a_list)

a_list = []

while True :
    try:
        n = int(input())
        a_list.append(n)
    except:
        break

insertion_sort(a_list)
ave = average(a_list)
print(ave)
index = len(a_list)//2
median = a_list[index]
print(median)
