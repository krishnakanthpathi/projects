from sortedcontainers import SortedList
n , k = map(int, input().split())
arr = list(map(int, input().split()))
window = SortedList()
res = l = 0 

for r in range(n) :
    window.add((arr[r] , r))
    while l <= r and  window[-1][0] - window[0][0] > k :
        window.discard((arr[l] , l))
        l += 1
    res += r - l + 1

print(res)