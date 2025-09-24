from collections import Counter

t = int(input())

for _ in range(t) :
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    hashmap = Counter([val%k for val in arr ])
    for val in hashmap :
        if hashmap[val] == 1 :
            for idx,num in enumerate(arr) :
                if num % k == val :
                    print("YES")
                    print(idx + 1)
                    break
            break
    else:
        print("NO")