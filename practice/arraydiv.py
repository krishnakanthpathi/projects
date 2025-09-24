n , k = map(int,input().split())
arr = list(map(int, input().split()))

def Check(target):
    cur = 0
    total = 1
    for val in arr :
        if cur + val > target :
            total += 1
            cur = val
        else:
            cur += val
        
    return total <= k 

res = -1
l = max(arr)
r = sum(arr)
while l <= r :
    mid = (l + r)//2
    cur = Check(mid)
    if cur:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
        
print(res)