# output:
t = int(input())
for _ in range(t):
    n , x = map(int , input().split())
    arr = list(map(int, input().split()))
    
    maxi = abs(0 - arr[0])
    for i in range(1 , n) :
        maxi = max(maxi , abs(arr[i] - arr[i - 1]))
    last = abs(x - arr[-1])*2
    print(max(maxi , last))
