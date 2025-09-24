import sys
import math
from collections import *


def main() :
    n =  int(input())
    arr = list(map(int , input().split()))
    def checker(target)  ->bool :
        trans = [0]*n
        for i in range(n - 1 , -1 ,-1):
            if trans[i] + arr[i] < target :
                return False
            diff= trans[i] + arr[i] - target 
            diff = min(diff ,arr[i])
            if i - 1 >= 0 and i - 2 >= 0  : trans[i - 1] += (diff//3)
            if i - 2 >= 0 and i - 2 >= 0  : trans[i - 2] += 2*((diff)//3)
            
            
        return True
     
    l = min(arr)
    r = max(arr)
    ans = -1
    while l <= r :
        mid = l + (r - l) // 2
        if checker(mid) :
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)



t = int(input())
for i in range(t) : main()