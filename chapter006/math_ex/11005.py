from string import ascii_uppercase

x1,x2 = input().split(" ")
x2 = int(x2)
x1 = int(x1)
list_36 = list(str(r) for r in range(10)) + list(ascii_uppercase)
list_x = list_36[:x2]
y_list =[]

while (x1 > 0) :
    y_list.insert(0,list_x[x1 % x2]) #나머지
    x1 = x1 // x2   #몫

str = ''.join(y_list)
print(str)

