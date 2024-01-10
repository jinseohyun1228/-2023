# 선형 탐색 (기본)

def linear_serch(a_list,n):
    for i in a_list:
        if i == n :
            return True
    return False

x1 = [1,5,4,6,7,21]
a = 7
b = 9
print(linear_serch(x1,a))
print(linear_serch(x1,b))

# 파이썬의 in 키워드를 이용한 선형 탐색
print(a in x1)
print(b in x1)