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
    arr = list(map(int , input().split()))
    l = res = cur = 0
    for r in range(n) :
        cur += arr[r]
        while cur > k :
            cur -= arr[l]
            l += 1
        nt = r - l + 1
        res = res + nt * (nt + 1)//2
    print(res)
    
    
main()