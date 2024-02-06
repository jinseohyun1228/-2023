"""
만약 해독된 암호문에서 원문이 단 한번만 등장하게 하는 암호화 방법
"no solution" : 조건을 만족하는 암호문의 시프트 값이 존재 x
unique: #  만족하는 시프트 값
"ambiguous: " 를 출력하고 그 뒤에 오름차순으로 정렬된 조건을 만족하는 시프트 값의 목록을 출력

4
알파벳 순서 / 원문/ 암호문

ABC / ABC / ABCBBBABC no solution

ABC / ABC / ABCBCAABC unique: 1

D7a / D7a / D7aaD77aDD7a ambiguous: 1 2

ABC / ABC / ABC unique: 0
"""