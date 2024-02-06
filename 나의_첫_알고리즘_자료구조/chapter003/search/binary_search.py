#기본 이진 탐색
def binary_search(a_list,n):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first+last) //2
        if a_list[mid] == n :
            return True
        elif a_list[mid] < n:
            first = mid + 1
        else:
            last = mid - 1 #⭐
    return False


x1 = [1,3,5,7,9,11,13]
a = 11
b = 2

print(binary_search(x1,a))
print(binary_search(x1,b))


#파이썬의 bisect_left를 이용한 이진 탐색
"""
bisect_left(리스트,목표) 
    : 반환 값 = 존재하면 있었을 인덱스
"""
from bisect import bisect_left

def binary_search_bisect(a_list,n):
    index = bisect_left(a_list,n)
    if a_list[index] == n:
        return True
    return False

print(binary_search_bisect(x1,a))
print(binary_search_bisect(x1,b))