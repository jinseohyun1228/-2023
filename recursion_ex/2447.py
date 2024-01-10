def star_recursion(total_n):
    if total_n < 3 :
        return
    n = total_n//3
    i = 0
    str = []
    while i < n :
        str.append("*"*total_n)
        i += 1
    while i < n*2 :
        str.append("*"*(n) + " "*(n) + "*"*(n))
        i += 1
    while i < n*3 :
        str.append("*" * total_n)
        i += 1
    return str


x1 = 9
b_list = star_recursion(x1)
print(b_list)



