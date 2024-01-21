a_list = []

for i in range(3):
    a_list.append(input())

result = 0

for i in range(len(a_list)):
    if a_list[i].isdigit():
        result = int(a_list[i]) + (3-i)
        break

r_3 = result % 3
r_5 = result % 5

if r_3 == 0 and r_5 == 0:
    print("FizzBuzz")
elif r_3 == 0:
    print("Fizz")
elif r_5 == 0:
    print("Buzz")
else:
    print(result)

"""
# 피즈버즈 값 확인하기
for i in range(50):
    i_3 = i % 3
    i_5 = i % 5
    if  i_3 == 0 and i_5 == 0 :
        print(i,": FizzBuzz")
    elif i_3 == 0:
        print(i,": Fizz")
    elif i_5 == 0:
        print(i, ": Buzz")
    else:
        print(i)
"""
