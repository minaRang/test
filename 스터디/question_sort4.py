import heapq
N=int(input())
heap=[]
result=0

for _ in range(N):
    heap.append(int(input()))
heapq.heapify(heap)

while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    result+=(a+b)

print(result)