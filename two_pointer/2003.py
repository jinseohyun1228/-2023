x1,x2=input().split(" ")
x1 = int(x1)
x2 = int(x2)

a_list=[int(i) for i in input().split(" ")]

start = 0
end = 0
count = 0

while start < len(a_list) and end < len(a_list):
    sum_lsit = sum(a_list[start:end+1])
    if sum_lsit == x2:
        if start == end:
            count += 1
            end += 1
        else:
            count += 1
            start += 1
    elif sum_lsit < x2:
        end += 1
    else:
        start += 1

print(count)
