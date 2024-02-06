import re
def number_extraction(str_list):
    a_list  = []
    i = 0
    temp = ""
    j = 0
    while i < len(str_list):
        if str_list[i] == ' ':
            i += 1
            if j == 1:
                a_list.append(temp)
                temp =""
                j = 0
        elif str_list != ' ':
            temp = temp + str_list[i]
            i += 1
            j = 1
    return a_list

string01 = "저는 3학년 2반 3번이에요"
string02 = "저는 3학년 2반 33번이에요"

string01_int = re.sub(r'[^0-9]',' ',string01)
str_list01 = list(str(string01_int))
print(str_list01)
a_list01 = number_extraction(str_list01)

# print(a_list01)

string02_int = re.sub(r'[^0-9]',' ',string02)
str_list02 = list(str(string02_int))

a_list02 = number_extraction(str_list02)

# print(a_list02)

print(a_list01[-1])
print(a_list02[-1])

################# 조건을 넣은 리스트 만들기######################

s = "나는 3학년 3반입니다."
new_list = [c for i in s if c.isdigit()]
print(new_list)