import sys
import math
from collections import *

def ask(left , right):
    print("?", left , right)
    sys.stdout.flush()
    arr = list(map(int ,input().split()))
    cnt = 0
    for val in arr :
        if left <= val <= right :
            cnt += 1
    return cnt%2 == 1

def tell(val):  
    print("!",val)
    

def main() :
    n =  int(input())
    l = 1
    r = n
    ans = -1
    while l<= r :
        mid = (l + r)//2
        if ask(l , mid) :
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    tell(ans)
    return


t = int(input())
for i in range(t) : main()