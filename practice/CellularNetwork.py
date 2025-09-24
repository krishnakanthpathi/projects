
n , k = map(int , input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

def upperbound(target):
    l = 0
    ans = float("inf")
    r = k - 1
    while l <= r :
        mid = (l + r) // 2
        # print(mid , target)
        if towers[mid] >= target :
            ans = towers[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans

def lowerbound(target):
    l = 0
    ans = float("inf")
    r = k - 1
    while l <= r :
        mid = (l + r) // 2
        if towers[mid] <= target :
            ans = towers[mid]
            l = mid + 1
        else:
            r = mid - 1
    return ans

res = -float("inf")
for val in cities :
    upper , lower = upperbound(val) , lowerbound(val)
    res = max(res , min(abs(val - upper) , abs(val - lower)))
print(res)