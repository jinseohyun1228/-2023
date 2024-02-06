from collections import deque

dq = deque([4,5,6])

dq.append(7)
dq.appendleft(3)
print(str(dq) + " #pop 연산 시작")
print(dq.pop())
print(dq.popleft())
print(str(dq) + " #pop 연산 끝")

dq.extend([7,8,9])
print(dq)
dq.extendleft([3,2,1])  # 요소하나하나를 추가한다.
print(dq)

dq.insert(4,5)
print(dq)

dq.remove(5)
print(dq)
dq.remove(5)
print(dq)

dq.reverse()
print(dq)

print(dq.index(9))          #0
# print(dq.index(222))        #ValueError


print(dq.count(0))      #0
print(dq.count(1))      #1

print(len(dq))          #8

print(dq)
dq.rotate(-1)
print(dq)
dq.rotate(2)
print(dq)

# dq.pop()            #IndexError:
# dq.popleft()        #IndexError:

# dq.remove(4)        #ValueError
