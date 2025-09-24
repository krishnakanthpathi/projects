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
    
    a1 , a2 , a4 , a5  = list(map(int , input().split()))
    # a1 + a2 = a3 or a4 + a3 = a5
    res1 = res2 = 1
    a12 = a1 + a2
    a45 = a5 - a4
    if a2 + a12 == a4 : res1 += 1
    if a4 + a12 == a5 : res1 += 1

    if a1 + a2 == a45 : res2 += 1
    if a2 + a45 == a4 : res2 += 1
    print(max(res1 , res2))

t = int(input())
for i in range(t) : main()