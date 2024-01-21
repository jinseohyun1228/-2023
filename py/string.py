lines = []

while True:
    line = input()
    if not line:
        break  # 빈 문자열이 입력되면 입력 종료
    lines.append(int(line))  # 입력 값을 정수로 변환하여 리스트에 추가

print(lines)

string01 = "안녕하세요. 저는 진서현입니다."
string01 = string01.replace(" ","")

print(string01)

string02 = "간장콩장장은 간콩장장?"
print(string02)
string02 = string02.replace("장","")
print(string02)

string03 = "안녕"
string04 = "안녕"

if string03 == string04:
    print(string03+ " == " + string04)
s = "안녕하세요"
print(len(s))

print(s[::-1])

string05 = "THE SUN SETS"
string05 = string05.lower()
print(string05)

string05 = string05.upper()
print(string05)
# 문자열 반으로 나누기
p = [0,1,2,3,4]
mid = len(p)//2
print(mid)
print(p[:mid])
print(p[mid:])

a_list = [1,3,5]
b_list = [6,7]

a_list.extend(b_list)
print(a_list)
a_list.append(b_list[0])
print(a_list)



print(s[1:-1])

a,b = input().split(",")
print(a)
print(b)

x = int(input())
x_list = [""] * x

for i in range(x):
    x_list[i] = input()

for i in range(x):
    print(x_list[i])