def main():
    n = int(input())
    arr = list(map(int ,input().split()))
    res = (arr[-1] - arr[0] )
    if n > 1 :
        res = max(res,max(arr[1:]) - arr[0])
        res = max(res,arr[-1] - min(arr[:-1]))
    
    for i in range(n - 1):
        res = max(res ,
            arr[i] - arr[i + 1] 
            )
    print(res)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()