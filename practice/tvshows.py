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
    n,k,d = list(map(int , input().split()))
    arr = list(map(int , input().split()))
    shows = defaultdict(int)
    l = 0
    res = 1e9
    for r in range(n):
        shows[arr[r]] += 1
        if r - l + 1 > d:
            shows[arr[l]] -= 1
            if shows[arr[l]] == 0:
                del shows[arr[l]]
            l += 1
        if r - l + 1 == d:
            res = min( res , len(shows))
    print(res)

t = int(input())
for i in range(t) : main()