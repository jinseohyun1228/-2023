# 시간 초과
def linear_serch(a_list,n):
    if n in a_list:
        return 1
    else:
        return 0


from sys import stdin
x1 = int(stdin.readline())
a_list = list(map(int,stdin.readline().split()))

x2 = int(stdin.readline())
t_list = list(map(int,stdin.readline().split()))



y_list = []
for i in t_list:
    y_list.append(linear_serch(a_list,i))

y_str = ' '.join(str(i) for i in y_list)

print(y_str)


