import math

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split("#")
    res = 0
    minval = float("inf")
    for val in arr :
        if len(val) >= 3 :
            minval = min(minval , 2)
            break
        else:
            res += len(val)
    if minval != float("inf") :
        print(minval)
    else:
        print(res)