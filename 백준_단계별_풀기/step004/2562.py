a_list = []

while True :
    try:
        n = int(input())
        a_list.append(n)
    except:
        break

max = a_list[0]
j = 0

for i,v in enumerate(a_list):
    if v > max:
        max = v
        j = i

print(max)
print(j+1)
