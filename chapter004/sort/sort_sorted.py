list_1 = [1,4,7,2,3,7]
list_1 = sorted(list_1)
print(list_1)   #[1, 2, 3, 4, 7, 7]
list_1 = sorted(list_1, reverse=True)
print(list_1)   #[7, 7, 4, 3, 2, 1]

list_2 = ["안녕","바보냐?","가격얼마에요?"]
list_2 = sorted(list_2)
print(list_2)   #['가격얼마에요?', '바보냐?', '안녕']
list_2 = sorted(list_2,key=len)
print(list_2)   #['안녕', '바보냐?', '가격얼마에요?']

list_3 = [5,7,3,8,1,4]
list_3.sort()
print(list_3)   #[1, 3, 4, 5, 7, 8]
list_3 = list_3.sort()
print(list_3)   #None