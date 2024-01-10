a = int(input())
numbers = [int(num) for num in input().split()]
numbers = sorted(numbers)
c = int(input())
check_numbers = [int(num) for num in input().split()]

#정렬했었어야 했다.
#발견하면 count += 1
#그리고 그 값 리스트에서 제거해야함
#그리고 다시 루프 돌려야 한다
#더이상 없으면 루프 나오고 넘어가게 해야 함

def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    count = 0
    while last >= first:
        mid = (last + first) // 2
        if a_list[mid] == n:
            count += 1
            a_list.remove(n)

            mid = (last + first) // 2
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return count

for i in check_numbers:
    print(binary_search(numbers, i))