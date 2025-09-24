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
    string = input()
    odd = []
    even = []
    for char in string :
        if int(char) % 2 == 0 :
            even.append(char)
        else :
            odd.append(char)
    res = []
    i = j = 0
    while i < len(odd) and j < len(even):
        if odd[i] < even[j]:
            res.append(odd[i])
            i += 1
        else:
            res.append(even[j])
            j += 1
    while i < len(odd):
        res.append(odd[i])
        i += 1
    while j < len(even):
        res.append(even[j])
        j += 1
    res = ''.join(res)
    print(res)

t = int(input())
for i in range(t) : main()


