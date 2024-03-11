from queue import Queue

q = Queue()
q.put(3)
q.put(2)
q.put(1)

print(q.qsize())    #3
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())    #0

