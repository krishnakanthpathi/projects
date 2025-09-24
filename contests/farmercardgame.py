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
    n , m = list(map(int , input().split()))
    arr= []
    for i in range(n) :
        temp = list(map(int , input().split()))
        cur = []
        for val in temp : cur.append((val, i + 1))
        arr.append(cur)
    for val in arr :
        val.sort()
    arr.sort()
    res = [ val[0][-1] for val in arr ]
    for j in range(m):
        for i in range(1,n):
            if arr[i][j][0] < arr[i-1][j][0] :
                print(-1)
                return -1
    print(*res)

t = int(input())
for i in range(t) : main()