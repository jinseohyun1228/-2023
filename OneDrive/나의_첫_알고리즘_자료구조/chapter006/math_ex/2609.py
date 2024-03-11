def find_the_value(x1,x2):
    if  x1 > x2 :
        small_num,big_num = x2,x1
    else:
        small_num, big_num = x1, x2

    greatest_common_divisor = 1
    i = 2

    while (i <= small_num):
        if small_num % i == 0 and big_num % i == 0 :
            greatest_common_divisor = i
        i += 1

    least_common_multiple = greatest_common_divisor * (small_num // greatest_common_divisor) * (big_num//greatest_common_divisor)

    return greatest_common_divisor,least_common_multiple


x1, x2 = input().split(" ")
x1 = int(x1)
x2 = int(x2)

y1,y2 = find_the_value(x1,x2)

print(y1)
print(y2)