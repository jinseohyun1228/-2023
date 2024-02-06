baskets,m = input().split(" ")
baskets = int(baskets)
basket_list = []

for i in range(baskets):
    basket_list.append(i+1)

m_list =[]
for i in range(int(m)):
    m_list.append([int(j) for j in input().split(" ")])

for i in m_list:
    basket_list[i[0]-1],basket_list[i[1]-1] = basket_list[i[1]-1],basket_list[i[0]-1]

print(*basket_list)