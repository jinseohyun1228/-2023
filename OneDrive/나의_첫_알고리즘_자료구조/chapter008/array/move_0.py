#교재에 있는 리스트에서 0 옮기기

## 직접 구현한 예제
a_list = [8,0,3,0,12]

def move_zero (a_list):
    temp = 0
    for i,v in enumerate(a_list):
        if v == 0 :
            temp = v
            while i < len(a_list)-1 :
                a_list[i] = a_list[i+1]
                i += 1
            a_list[-1] = v

move_zero(a_list)
print(a_list)

#교재 정답
def move_zero_textbook00(a_list):
    zero_index = 0
    for index,v in enumerate(a_list):
        if v != 0:  #해당 원소의 값이 0이 아닐 때
            a_list[zero_index] = v      # zero_index의 위치에 원소 대입
            if zero_index != index:     # zero_index가 현재의 인덱스값과 다를 때
                a_list[index] = 0       # 현재 인덱스에는 0을 대입
            zero_index += 1             # zero_index 증가
    return a_list

c_list = [0,1,2,0,45,0,50]
move_zero_textbook00(c_list)
print(c_list)

## 교재의 예제 알고리즘 변형해보기 - 틀렸다
def move_zero_textbook01(a_list):
    zero_index = 0
    for index,v in enumerate(a_list):
        if v != 0:  #해당 원소의 값이 0이 아닐 때
            a_list[zero_index] = v      # zero_index의 위치에 원소 대입
            if zero_index != index:     # zero_index가 현재의 인덱스값과 다를 때
                a_list[index] = 0       # 현재 인덱스에는 0을 대입
            zero_index = index             # zero_index 는 현재 인덱스
        else:
            zero_index = index
    return a_list

b_list = [0,1,2,0,45,0,50]
move_zero_textbook01(b_list)
print(b_list)

"""
    []/zero
0 : [0,1,2,0,45,0,50]/0
1 : [1,0,2,0,45,0,50]/1
2 : [1,2,0,0,45,0,50]/2
3 : [1,2,0,0,45,0,50]/2
4 : [1,2,45,0,0,0,50]/3 
📌 문제 발생 (이전의 zero_index와 현재 index사이에 0이 존재할 수 있다. 
5 : 
6 :
"""

