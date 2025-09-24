n , k = map(int , input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))

l = 0
r = max(arr)
error = 1e-7
ans = -1

def check(length):
    cnt = 0
    for val in arr :
        cnt += val//length
    return cnt >= k

for i in range(55) :
    mid = (l + r)/2

    if check(mid) :
        ans = mid
        l = mid + error
    else:
        r = mid - error

print(ans)

