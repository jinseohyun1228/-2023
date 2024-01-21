x1 = [int(i) for i in input().split(" ")]

if x1[0] == x1[1]:
    print("==")
elif x1[0] < x1[1]:
    print("<")
else:
    print(">")