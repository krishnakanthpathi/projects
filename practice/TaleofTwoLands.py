n = int(input())
arr = list(map(int , input().split()))

lands = []
for val in arr :
    lands.append(abs(val))

def lowerbound(target) :
    l = 0
    r = n - 1
    ans = -1
    while l <= r :
        mid = (l + r)//2
        if  lands[mid] <= target :
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

lands.sort()
res = 0
for idx,val in enumerate(lands) :
    lower = lowerbound( val * 2 )
    res += (lower - idx)

print(res)