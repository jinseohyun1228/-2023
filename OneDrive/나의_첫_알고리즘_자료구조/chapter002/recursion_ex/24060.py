# 24060 병합 정렬 문제
#병합 정렬:
def merge_sort(a_list):
    r = 0
    t_list = []
    if (len(a_list) > 1):
        mid = len(a_list) // 2
        left_list = a_list[:mid]
        right_list = a_list[mid:]
        a,b = merge_sort(left_list)
        r += a
        t_list.extend(b)

        c,d = merge_sort(right_list)
        r += c
        t_list.extend(d)

        a_list_i = 0
        left_i = 0
        right_i = 0

        while left_i < len(left_list) and right_i < len(right_list):
            if(left_list[left_i] <= right_list[right_i]) :
                a_list[a_list_i] = left_list[left_i]
                t_list.append(left_list[left_i])
                left_i += 1
            else:
                a_list[a_list_i] = right_list[right_i]
                t_list.append(right_list[right_i])
                right_i += 1
            a_list_i += 1
            r += 1

        while left_i < len(left_list):
            a_list[a_list_i] = left_list[left_i]
            t_list.append(left_list[left_i])
            left_i += 1
            a_list_i += 1
            r += 1


        while right_i < len(right_list):
            a_list[a_list_i] = right_list[right_i]
            t_list.append(right_list[right_i])
            right_i += 1
            a_list_i += 1
            r += 1

    return r,t_list

x1,x2 = input().split( )
x1 = int(x1)
x2 = int(x2)

a_list = list(map(int,input().split()))

r,t_list = merge_sort(a_list)
print(t_list)

if( x2 > len(t_list)):
    print(-1)
else:
    print(t_list[x2-1])


