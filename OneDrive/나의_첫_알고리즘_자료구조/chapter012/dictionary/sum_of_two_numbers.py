def two_sum_brute(a_list,target):
    dic = {}
    count = 0
    for i, n in enumerate(a_list):
        x = target - n
        if x in dic :
            count += 1
            dic[n] = i
        else:
            dic[n] = i
    return count


a_list = [1,2,3,4,5,6]

print(two_sum_brute(a_list,7))  #3
print(two_sum_brute(a_list,6))  #2
print(two_sum_brute(a_list,4))  #1
print(two_sum_brute(a_list,1))  #0