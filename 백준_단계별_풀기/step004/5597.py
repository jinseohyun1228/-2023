student_list = list(range(1,31))

for i in range(28):
    student = int(input())
    student_list.remove(student)

print(student_list[0])
print(student_list[-1])

