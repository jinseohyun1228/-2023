def find_start(b_string):
    b_list = list(str(b_string))
    for i in range(len(b_list)):
        index = b_list.index(i,i+1,len(b_list))
def find_string(a_list,b_list):
    a = 0
    b = 0
    e = 0
    while True:
        if a_list[a] == b_list[b]:
            a += 1
            b += 1
        else:
            






x1_list = "ABC ABCDAB ABCDABCDABDE"
x2_list = "ABCDABD"


find_string()

