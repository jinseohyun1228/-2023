from heapq import heapify,heappop,heappush

rope_heap = [1,3,5,7]
heapify(rope_heap)

total_cost = 0

while len(rope_heap) > 1:
    temp_cost = heappop(rope_heap) + heappop(rope_heap)
    total_cost += temp_cost
    heappush(rope_heap,temp_cost)

print(total_cost)

