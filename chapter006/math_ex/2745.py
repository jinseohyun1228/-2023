from string import ascii_uppercase

x1,x2 = input().split(" ")
x2 = int(x2)
x_list = list(x1)

list_36 = list(str(r) for r in range(10)) + list(ascii_uppercase)
y = 0

for i in range(len(x_list)):
    y += list_36.index(x_list[i]) * (x2**(len(x_list)-1 - i))

print(y)

