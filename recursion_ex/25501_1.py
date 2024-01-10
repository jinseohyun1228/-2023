# 25501번
"""
첫째 줄에 테스트케이스의 개수 $T$가 주어진다.
둘째 줄부터 $T$개의 줄에 알파벳 대문자로 구성된 문자열 $S$가 주어진다.
"""

def palindrome(s):
    s_len = len(s)
    i = 0

    while i < (s_len-1)/2 :
        if (s[i-1] != s[-i]) :
            return 0
        i += 1
    return 1


x = int(input())
x_list = [""] * x

for i in range(x):
    x_list[i] = input()

for i in range(x):
    print(palindrome(x_list[i]))
