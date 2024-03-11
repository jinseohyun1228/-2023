import random
import time


def bubble_sort(a_list):
    temp = 0
    for i in range(len(a_list)-1):
        for j in range(len(a_list)-1):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]

    return a_list

def bubble_sort_1(a_list):
    for i in range(len(a_list)-1):
        for j in range((len(a_list)-1) - i):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]

    return a_list

def bubble_sort_2(a_list):
    temp = 0
    for i in range(len(a_list)-1):
        count = 0
        for j in range((len(a_list)-1) - i):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
                count += 1
        if count == 0:
            return a_list
    return a_list

a_list_0 = [random.randint(0,200000) for i in range(0,5000)]
a_list_1 = [random.randint(0,200000) for i in range(0,5000)]
a_list_2 = [random.randint(0,200000) for i in range(0,5000)]

start_0 = time.time()
bubble_sort(a_list_0)
end_0 = time.time()

start_1 = time.time()
bubble_sort_1(a_list_1)
end_1 = time.time()

start_2 = time.time()
bubble_sort_2(a_list_2)
end_2 = time.time()

print(f"{end_0 - start_0:.5f} sec" )
print(f"{end_1 - start_1:.5f} sec" )
print(f"{end_2 - start_2:.5f} sec" )