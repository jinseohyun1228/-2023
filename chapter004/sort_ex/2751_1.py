

x1 = int(input())

a_list = []
while True :
    try:
        n = int(input())
        a_list.append(n)
    except:
        break

a_list.sort()


for i in a_list:
    print(i)
