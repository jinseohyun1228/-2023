b_list = list(str("ABABD"))
result = 0
for i in range(len(b_list)):
    try:
        index = b_list.index(b_list[i],i+1,len(b_list))
        result = index
    except ValueError:
        break





