import sys
import math
from collections import *

def ask(left , right):
    print("?", *([left , right]))
    sys.stdout.flush()
    return int(input())

def tell(val):  
    print("!",val)
    

def main() :
    n =  int(input())
    l = 1
    ans = None
    r = n
    while l < r :
        sec = ask(l , r)

        if r - l + 1 == 2 :
            if sec == l :
                tell(r)
            else:
                tell(l)
            return
        
        mid = (l + r)//2
        
        if sec <= mid :
            left = ask(l , mid)
            if left == sec :
                r = mid
            else:
                l = mid
        else:
            right = ask(mid  , r)
            if right == sec :
                l = mid
            else:
                r = mid 

    tell(ans)
    return ans
# 5 1 4 2 3
#     |
#     p
# 4 3 2 1 5 6


main()