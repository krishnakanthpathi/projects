t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for val in arr :
        if val == 0 :
            cnt +=1

    if cnt == n :
        print(0)
    else:
        i = 0
        temp = 0
        while i < n and arr[i] == 0 :
            temp += 1
            i += 1
            
        j = n - 1
        while j >= 0 and arr[j] == 0 :
            temp += 1
            j -= 1
            
        if temp == cnt :
            print(1)
        else:
            print(2)
