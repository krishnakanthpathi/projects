import sys
import math
from collections import *


def main() :
    n , k =  list(map(int , input().split()))
    arr = list(map(int , input().split()))
    total = sum(arr)
    arr.sort()
    prefix = [ 0 ]
    for val in arr :
        prefix.append(prefix[-1] + val)
    def checker(target) -> bool:
        if total <= k:
            return True

        # Simulate replacing `target` largest elements with the smallest
        mini = float("inf")
        for i in range(target + 1):
            rem = target - i
            if n - rem <= 0:
                continue  # Out of bounds check
            prefixsum = prefix[n] - prefix[n - rem]  # Sum of largest `rem` elements
            replaced_sum = total - prefixsum + rem * (arr[0] - i) - i
            mini = min(mini, replaced_sum)

        return mini <= k
#     def checker(target)  ->bool :
#         if total <= k :
#             return True
#         if target > n  :
#             temp = arr[0] - (target - (n - 1))
#             return temp * n <= k
        
#         mini = float("inf")
#         # 1 1 1 1 2 2 3 target = 2 total = 10
#         # |           rem 1 ,

#         for i in range(0 , target + 1):
#             rem = target - i
#             prefixsum = prefix[n] - prefix[n - rem]
#             mini = min(
#                 mini ,
#                 total - i + rem * ( arr[0] - i ) - (prefixsum - arr[0] )
#             )
#         return mini <= k

    l = 0 
    r = total
    ans = -1
    while l <= r :
        mid = l + (r - l) // 2
        if checker(mid) :
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)



t = int(input())
for i in range(t) : main()