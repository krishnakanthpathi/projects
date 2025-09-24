t = int(input())

for _ in range(t) :
    n , k = map(int,input().split())
    arr = []
    for i in range(n) : arr.append(input())
    i = 0
    while k > 0 and i < len(arr):
        if len(arr[i]) <= k :
            k -= len(arr[i])
            i += 1
        else:
            break
    print(i)