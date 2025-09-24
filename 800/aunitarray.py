import sys
import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    neg = sum(1 for i in a if i < 0)
    pos = sum(1 for i in a if i > 0)
    
    diff = neg - pos 
    if diff > 0 :
        ceiled = diff // 2
        if neg - ceiled > pos + ceiled:
            ceiled += 1
        
        print(ceiled if (neg - ceiled)% 2 == 0 else min(n , ceiled + 1))
        sys.stdout.flush()
    else:
        print(1 if neg % 2 != 0 else 0)
        sys.stdout.flush()