# 병합 정렬:
def merge_sort(a_list):
    if len(a_list) > 1:
        # 파이썬의 //는 정수 몫을 구하는 연산자
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)


        left_ind = 0
        right_ind = 0
        alist_ind = 0

        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else: #오른쪽 첫번째 요소가 더 작은 경우
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1

            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1
    return a_list


a_list = [6,3,2,10,-10]
merge_sort(a_list)
print(a_list)
