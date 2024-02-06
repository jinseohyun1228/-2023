x = int(input())

score_list = [int(i) for i in input().split(" ")]

score_list.sort()
max = score_list[-1]
total = 0
for i in score_list:
    total += i/max*100

print(total/x)
