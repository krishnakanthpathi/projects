n , k = map(int,input().split())
arr = list(map(int, input().split()))

def Check(target):
    total = 0
    for val in arr :
        total += target //  val
        if total >= k :
            return True
    return False

res = -1
l = 0
r = min(arr) * k
while l <= r :
    mid = (l + r)//2
    cur = Check(mid)
    if cur:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
        
print(res)