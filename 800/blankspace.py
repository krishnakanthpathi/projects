import sys
import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = float('-inf')
    curr = 0
    for i in range(n):
        curr = curr + 1 if a[i] == 0 else 0
        res = max(res, curr)
        
            
    sys.stdout.write(str(res) + "\n")
    sys.stdout.flush()