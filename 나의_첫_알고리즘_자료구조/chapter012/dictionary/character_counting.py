def character_counting(a_string):
    dic = {}
    for i in a_string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

a_str = "Be Happy~!"

print(character_counting(a_str))
#{'B': 1, 'e': 1, ' ': 1, 'H': 1, 'a': 1, 'p': 2, 'y': 1, '~': 1, '!': 1}

