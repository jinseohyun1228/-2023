num_list = []
for i in range(10):
    num_list.append(int(input()))

div_set = set()

for i in num_list:
    div_set.add(i%42)

print(len(div_set))

