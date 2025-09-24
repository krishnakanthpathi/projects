# output:

t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    arr = list(map(int, input().split()))
    
    if k < 2 :
        if arr != sorted(arr):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
