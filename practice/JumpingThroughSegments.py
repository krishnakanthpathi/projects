t = int(input())
for _ in range(t) :
    n = int(input())
    arr = []
    for _ in range(n) :
        arr.append(list(map(int , input().split())))


    def check(k):
        left = right = 0
        for l , r in arr :
            left = left - mid
            right = right + mid
            left = max(left , l)
            right = min(r , right)
            if left > right :
                return False
        return True

    ans = -1
    l = 0
    r = int(1e9)
    while l <= r :
        mid = (l + r)//2
        if check(mid) :
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
