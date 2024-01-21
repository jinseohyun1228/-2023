def find_index(num):
    binary = format(num, 'b')
    binary = list(str(binary))
    binary_reverse = binary[::-1]
    s = ""
    for i in range(len(binary_reverse)):
        if binary_reverse[i] == "1":
            s = s + str(i) + " "

    return s

x1 =  int(input())
num_list = []
for i in range(x1):
    num_list.append(int(input()))

s = ""
for i in num_list:
    s = s + find_index(i) +"\n"

print(s)

