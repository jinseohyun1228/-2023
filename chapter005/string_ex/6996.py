def anagram(a_list):
    a1_list = list(str(a_list[0]))
    a2_list = list(str(a_list[1]))
    print(a2_list)

    if (len(a1_list) != len(a2_list)):
        return False

    a1_list.sort()
    a2_list.sort()

    for i in range(len(a1_list)):
        if (a1_list[i] != a2_list[i]):
            return False

    return True


x1 = int(input())
a_lsit = [""] * x1

for i in range(x1):
    a_lsit[i] = input().split(" ")


for i in a_lsit:
    if(anagram(i)):
        print(i[0]+" & "+ i[1] + " are anagrams.")
    else:
        print(i[0] + " & " + i[1] + " are NOT anagrams.")
