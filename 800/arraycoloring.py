t = int(input())
for _ in range(t):
    n = int(
        input()
    )
    arr = list(map(int, input().split()))
    res = 0
    for val in arr :
        res  += val%2
    if res % 2 == 0 :
        print("YES")
    else:
        print("NO")