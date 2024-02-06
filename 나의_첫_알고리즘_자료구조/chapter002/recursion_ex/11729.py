# 백준 11729문제

def hanoi(num, from_, to, other):
    result = []
    if num == 0 : return 0
    hanoi(num-1,from_,other,to)
    print(str(from_) + " " + str(to))
    hanoi(num-1,other, to, from_)

x = int(input())
print(2**x-1)
hanoi(x,1,3,2)
