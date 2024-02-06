b,m = input().split(" ")
b = int(b)
basket_list = list(range(1,b+1))

m_list =[]
for i in range(int(m)):
    m_list.append([int(j) for j in input().split(" ")])

def reverse_list(a_list, start=0, end=None):
    if end is None:
        end = len(a_list) - 1

    if start < end:
        a_list[start], a_list[end] = a_list[end], a_list[start]
        reverse_list(a_list, start + 1, end - 1)

for i in m_list:
    reverse_list(basket_list,i[0]-1,i[1]-1)

print(*basket_list)