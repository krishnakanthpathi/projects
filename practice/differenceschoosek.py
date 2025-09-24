
from collections import *

def main() :
    n , k , m = list(map(int , input().split()))
    arr = list(map(int , input().split()))
    hashmap = defaultdict(list)
    res = 0 
    for i in range(n) :
        cur = arr[i] % m
        hashmap[cur].append(arr[i])
    for key in hashmap :
        if len(hashmap[key]) >= k :
            print("Yes")
            print(*hashmap[key][:k])
            return

    print("No")
main()