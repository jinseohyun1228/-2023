"""
#최대 공약수구하기
"""

x1,x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)

if x1 > x2 :
    x1,x2 = x2,x1

y_1 = x2-x1

str = '1' * y_1

print(str)