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
    n,a,b= list(map(int , input().split()))
    if a < b :
        diff = b - a - 1
        if diff%2 == 0 :
            print("NO")
        else:
            print("YES")
    else:
        diff = a - b - 1
        if diff%2 == 0 :
            print("NO")
        else:
            print("YES")

    

t = int(input())
for i in range(t) : main()