x1 = input()
x1 = list(str(x1))
x1_duplicate_remove = list(set(x1))
x1_duplicate_remove = sorted(x1_duplicate_remove,reverse=True)
x1_list = []
e = 0

for i in range(len(x1_duplicate_remove)):
    temp = []
    temp.append(x1_duplicate_remove[i])
    temp.append(x1.count(x1_duplicate_remove[i]))
    d = x1.count(x1_duplicate_remove[i])
    if d % 2 == 1:
        e += 1
    x1_list.append(temp)

str = []
if e > 1 :
    print("I'm Sorry Hansoo")
else:
    for i in x1_list:
        if int(i[1]) % 2 == 0:
            for j in range(i[1]//2):
                str.append(i[0])
                str.insert(0,i[0])
        else:
            for j in range(i[1]//2):
                str.append(i[0])
                str.insert(0,i[0])
            str.insert(len(str)//2,i[0])
    print(''.join(str))