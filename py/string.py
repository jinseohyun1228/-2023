s = "안녕하세요"
print(len(s))

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