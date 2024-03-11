"""
딕셔너리 {Key1: Value1, Key2: Value2, Key3: Value3}
- 키 값은 고유하다.
- 딕셔너리는 키를 통해서만 값에 접근할 수 있다.
"""

dic = { 1:"1", 2:"2", 3:"3"}
print(dic)      #{1: '1', 2: '2', 3: '3'}

#값 추가
dic[4] = "4"
print(dic)      #{1: '1', 2: '2', 3: '3', 4: '4'}

#값 삭제하기
del dic[4]
print(dic)      #{1: '1', 2: '2', 3: '3'}


#값 접근하기
a = dic[3]      #'3'
print(a)
#b = dic[4] 없는 키에 접근하면 KeyError: 4

print(dic.get(4))                   #None
print(dic.get(4,"없어요!"))          #없어요!

#해당 키가 딕셔너리 안에 있는지 조사하기
print(4 in dic)     #False
print(3 in dic)     #True

dic[3] = "삼"
print(dic)      #{1: '1', 2: '2', 3: '삼'}

#dict_keys 객체 반환
print(dic.keys())       #dict_keys([1, 2, 3])

#dict_values
print(dic.values())     #dict_values(['1', '2', '삼'])
#dict_items
print(dic.items())      #dict_items([(1, '1'), (2, '2'), (3, '삼')])

#지우기
print(dic.clear())      #None
