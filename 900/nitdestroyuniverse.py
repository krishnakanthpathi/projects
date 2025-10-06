def main() :
    n = int(input())
    arr = list(map(int ,input().split()))
    i = 0
    j = n - 1
    res = 0
    if all(x == 0 for x in arr) :
        print(0)
        return
    while i < n and arr[i] == 0 :
        i += 1
    while j >= 0 and arr[j] == 0 :
        j -= 1
    
    for k in range(i , j + 1) :
        if arr[k] == 0 :
            print(2)
            return 
    
    print(1)
    
if __name__ == "__main__" :
    t = int(input())
    for i in range(t) :
        main()