import string
# from sortedcontainers import SortedList
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from typing import List, Set, Tuple, Optional
from itertools import pairwise, permutations, combinations
from heapq import heappush, heappop
from random import shuffle
from functools import cmp_to_key, lru_cache
from fractions import Fraction

def main() :

    n , k = list(map(int , input().split()))
    a = list(map(int , input().split()))
    h = list(map(int , input().split()))
    l = fruits = res =  0
    prev = None
    for r in range(n) :
        fruits += a[r]
        while fruits > k :
            fruits -= a[l]
            l += 1
        if prev != None and  prev%h[r] != 0 :
            prev = h[r]
            fruits = a[r]
            if fruits <= k :
                res = max(res , 1)
            l = r
        else:
            res = max(res , r - l + 1)
            prev = h[r]
    print(res)

t = int(input())
for i in range(t) : main()