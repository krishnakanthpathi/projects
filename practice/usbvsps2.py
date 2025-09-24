from collections import defaultdict
import heapq

a , b ,c = map(int ,input().split())
m = int(input())
hashmap = defaultdict(list)


for i in range(m) :
    temp = input().split()
    x = int(temp[0])
    y = temp[-1]
    hashmap[y].append(x)

heapq.heapify(hashmap["USB"])
heapq.heapify(hashmap["PS/2"])  

res = 0
cnt = 0
while a > 0 and len(hashmap["USB"]) > 0 :
    a -= 1
    cnt += 1
    res += heapq.heappop(hashmap["USB"])

while b > 0 and len(hashmap["PS/2"]) > 0 :
    cnt += 1
    b -= 1
    res += heapq.heappop(hashmap["PS/2"])

while c > 0  :
    heap1 = float("inf") if len(hashmap["USB"]) == 0 else hashmap["USB"][0]
    heap2 = float("inf") if len(hashmap["PS/2"]) == 0 else hashmap["PS/2"][0]  
    if heap1 < heap2 and hashmap["USB"] :
        res += heapq.heappop(hashmap["USB"])
        cnt += 1
    elif hashmap["PS/2"] :
        res += heapq.heappop(hashmap["PS/2"])
        cnt += 1
    c -= 1

print(cnt , res)