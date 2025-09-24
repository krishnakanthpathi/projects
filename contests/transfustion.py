t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    total = sum(arr)
    cur = total//n
    if total%n != 0 :
        print("NO")
    else:
        temp = arr[::2]
        stepsum = sum(temp)
        remsum = total - stepsum
        if remsum != cur*(len(arr) - len(temp)) or stepsum != cur*len(temp) :
            print("NO")
        else:
            print("YES")
