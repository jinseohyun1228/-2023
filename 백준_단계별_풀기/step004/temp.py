i = [0]*9
print(i)

list = [0,1,2,3,4,5]

print(list[1:-1])

def reverse_list_recursive(a_list, start=0, end=None):
    if end is None:
        end = len(a_list) - 1

    if start < end:
        a_list[start], a_list[end] = a_list[end], a_list[start]
        reverse_list_recursive(a_list, start + 1, end - 1)

# 예제 사용법
my_list = [1, 2, 3, 4, 5]
reverse_list_recursive(my_list)
print(my_list)