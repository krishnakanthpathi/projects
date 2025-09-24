import math
n = int(input())

def Check(target):
    total = 0
    for i in range(1 , n + 1) :
        total += min(n ,target//i)
    return total >= math.ceil((n * n)/2)

res = -1
l = 1
r = n * n
while l <= r :
    mid = (l + r)//2
    cur = Check(mid)
    if cur:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
        
print(res)