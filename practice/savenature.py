import sys
import math
from collections import *


def main() :
    n =  int(input())
    arr = list(map(int , input().split()))
    x , a = list(map(int , input().split()))
    y , b = list(map(int , input().split()))
    k =  int(input())
    if x > y :
        a , b = b , a
        x , y = y , x
    arr.sort(reverse=True)
    def check(target) :
        res = 0
        lcm = ( a * b ) // math.gcd(a, b)
        acount = target//a - target//lcm
        bcount = target//b - target//lcm
        abcount = target//lcm
        i = 0
        while abcount > 0 :
            res += arr[i] * (x + y)/100
            abcount -= 1
            i += 1
        while bcount > 0 :
            res += arr[i] * (y)/100
            bcount -= 1
            i += 1
        while acount > 0 :
            res += arr[i] * (x)/100
            acount -= 1
            i += 1

        return res >= k
    l = 1
    r = len(arr)
    ans = -1
    while l <= r :
        mid = ( l + r ) // 2 
        if check(mid):
            ans = mid 
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
        
t = int(input())
for i in range(t) : main()