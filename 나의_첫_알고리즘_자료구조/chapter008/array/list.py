# 교재 예제

## 0을 움직이고 기존 리스트 순서 유지하기

def move_zeros(a_list):
    zero_index = 0
    for i,v in enumerate(a_list):
        if v != 0:
            a_list[zero_index] = v
            if zero_index != i: #변동이 있었다는 뜻...?
                a_list[i] = 0
            zero_index += 1
        return a_list


## 리스트 결합하기
cobine_list01 = ["가나","토마토","생수"]
cobine_list02 = [1,2]

cobine_list = list(zip(cobine_list01,cobine_list02)) #둘 중 리스트의 크기가 작은 것에 맞추어서

print(cobine_list)

## 중복 요소 찾기
def find_duplicate_elements(a_list):
    a_set = set()
    temp = 0
    for i in a_list:
        original_length = len(a_set)
        a_set.add(i)
        if original_length == len(a_set):
            temp += 1
    return list(a_set),temp

duplicate_list = [0,1,1,3,3,3,4]
duplicate_removal_list,a = find_duplicate_elements(duplicate_list)

print(duplicate_removal_list,a)

# 교재에 있던 예제인데, 중복 요소를 반환한다. 중복이 여러개일경우 여러개를 출력해서 리팩토링해봄
def retrun_dup(a_list):
    dup = set()
    a_set = set()

    for i in a_list:
        l1 = len(a_set)
        a_set.add(i)
        l2 = len(a_set)
        if l1==l2:
            dup.add(i)

    return list(dup)

y = retrun_dup(duplicate_list)
print(y)

###################
## 두 리스트의 교집합 찾기

def make_inter_list(a_list,b_list):
    new_list = [v for v in a_list if v in b_list]
    return new_list

list1 = [1,3,4,5,6]
list2 = [3,4,5]

list3 = make_inter_list(list1,list2)
print(list3)

set1 = set(list1)
set2 = set(list2)

list3_1 = list(set1.intersection(set2))

print(list3_1)