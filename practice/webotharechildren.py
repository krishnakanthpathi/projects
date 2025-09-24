import math
import collections 
def main() :
    n = int(input())
    arr = list(map(int , input().split()))
    freq = collections.defaultdict(int)
    for val in arr :
        freq[val] += 1

    N = 2*1e5
    res = [0] * int(N + 1)
    for val in freq :
        if val == 1 :
            continue
        for i in range(val , int(N) + 1 , val ):
            res[i] += 1 * freq[val]

    print(max(res[:n + 1] ) + freq[1])

t = int(input())
for i in range(t) : main()