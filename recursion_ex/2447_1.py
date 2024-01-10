

def star(t,n,m):
    i = t//3
    if i <= n and i < n and i <= m and i < m :
        return " "
    return "*"

def star_recursion(t):
    str = ""
    for i in range(t):
        for j in range(t):
            str += star(t,i,j)
        str += "\n"
    return str

x1 = int(input())
str = star_recursion(x1)

print(str)

