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
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))

    prefix = [0] * (n + 1)
    for i in range(n) :
        cur = a[i]
        if a[i] < b[i] :
            diff = b[i] - a[i]
            
        
        


t = int(input())
for i in range(t) : main()