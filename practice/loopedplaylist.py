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
    n, k = list(map(int , input().split()))
    arr = list(map(int, input().split()))
    total = sum(arr)
    minsongs = float("inf")
    songs = k//total
    if k%total == 0 : 
        print(*[1 , songs*n])
        return
    rem = k%total 
    for i in range(n):
        cur = 0
        cnt = 0
        for j in range(i , i + n):
            if cur >= rem :
                break
            cnt += 1
            cur += arr[j%n]
        if cnt < minsongs :
            minsongs = cnt
            start = i + 1
    print(start ,(songs)*n + minsongs)
main()