#문자열을 뒤집는 세가지 방법

#리스트로
a = "안녕?"
a = a[::-1] #?녕안
print(a)
#.join을 이용해서
b = ''.join(reversed("안녕하세요"))
print(b)       #요세하녕안
#스택을 이용해서

def reverse_string(a_string):
    stack = []
    s = ""
    for i in a_string:
        stack.append(i)
    while len(stack) != 0:
        s += str(stack.pop())
    return s
"""
    for i in stack:
        print(i)
        s += str(stack.pop())
    return s
"""
a_list = "안녕하십니까"
print(reverse_string(a_list))