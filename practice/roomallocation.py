
import heapq


n = int(input())
 
intervals = []
for i in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b , i))
    
intervals.sort()
rooms = [0] * n
available = []
queue = []
for i in range(1, n+1):
    heapq.heappush(available, i)

for i in range(n):
    a, b, index = intervals[i]
    while queue and a > queue[0][0] :
        heapq.heappush(available, heapq.heappop(queue)[-1])

    alloc = heapq.heappop(available)
    rooms[index] = alloc
    heapq.heappush(queue, (b , alloc))
    
print(len(set(rooms)))
print(*rooms)