def meke_list(total_n):
    total_list = []
    n = total_n//3
    for i in range(total_n):
        row = ["*"] * total_n
        total_list.append(row)
    return total_list

def star(t,n,m):
    i = t//3
    if i <= n and i < n and i <= m and i < m :
        return " "
    return "*"

def star_recursion(a_list,t):
    str = ""
    for i in range(t):
        for j in range(t):
            str += star(t,i,j)
        str += "\n"
    return str

x1 = int(input())
str = star_recursion(x1)

print(str)
x1 = 9
a_list = meke_list(x1)
print(a_list)
b_list = star_recursion(a_list,x1)
print(b_list)
