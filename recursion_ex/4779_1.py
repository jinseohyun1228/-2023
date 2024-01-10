def cantor(x_list):
    if ( len(x_list) <= 1 ):
        return x_list
    a = int(len(x_list)/3)
    t_list = " " * a
    x_list = cantor(x_list[:a]) + t_list + cantor(x_list[-a:])
    return x_list

def x_list_creat(n) :
    c_str = "-"
    i = 0
    x_list = c_str*(3**n)
    return x_list

a_list = []

while True :
    try:
        n = int(input())
        a_list.append(n)
    except:
        break

for i in a_list:
    print(cantor(x_list_creat(i)))

