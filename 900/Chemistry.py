from collections import Counter
t = int(input())


for _ in range(t):
    n , k = map(int, input().split())
    a = input()
    hashmap = Counter(a)
    # print(hashmap)
    larget_odd = even = 0
    total = 0
    for key in hashmap:
        if hashmap[key] % 2 == 1:
            larget_odd = max(larget_odd, hashmap[key])
            total += hashmap[key]
        else:
            even += hashmap[key]
    total -= larget_odd
    if k == total :
        print("YES")
    elif k < total:
        print("NO")
    else:
        k2 = k - total
        if k2 <= even + larget_odd :
            print("YES")
        else:
            print("NO")