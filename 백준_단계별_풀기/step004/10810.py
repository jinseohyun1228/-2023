baskets,m = input().split(" ")
baskets = int(baskets)

m_list =[]
for i in range(int(m)):
    m_list.append([int(j) for j in input().split(" ")])

baskets_list = [0]*baskets

for i in m_list:
    for j in range(i[0]-1,i[1]):
        baskets_list[j] = i[2]

print(*baskets_list)




