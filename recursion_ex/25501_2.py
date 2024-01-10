def palindrome(s,r):
    if(len(s) <= 1):
        return 1,r
    if(s[0] != s[-1]):
        return 0,r
    return palindrome(s[1:-1],r+1)



x = int(input())
x_list = [""] * x

for i in range(x):
    x_list[i] = input()

for i in range(x):
    a,b = palindrome(x_list[i],1)
    print(a, b)