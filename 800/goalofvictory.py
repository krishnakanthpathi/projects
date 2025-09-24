t = int(input())
for _ in range(t):
    n = int(input())
    efficiencies = list(map(int, input().split()))
    res = 0
    for val in efficiencies :
        res += val

    print(-res)
