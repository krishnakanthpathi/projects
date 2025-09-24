import sys
import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = [a[0]]

    for i in range(1, n):
        res.append(a[i] + a[i-1])
    sys.stdout.write(" ".join(map(str, res)) + "\n")
    sys.stdout.flush()