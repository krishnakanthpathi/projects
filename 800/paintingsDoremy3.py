t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int  , input().split()))
    hashmap = {}
    for val in arr :
        hashmap[val] = 1 + hashmap.get(val , 0)
    if len(hashmap) > 2 :
        print("NO")
    elif len(hashmap) == 1 :
        print("YES")
    else:
        arr = list(hashmap.values())
        if abs(arr[0] - arr[1]) <= 1 :
            print("YES")
        else:
            print("NO")