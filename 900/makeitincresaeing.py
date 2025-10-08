def main():
    n = int(input())
    arr = list(map(int ,input().split()))
    cnt = 0
    for i in range(n - 2 , -1 , -1):
        while arr[i] >= arr[i + 1] :
            if arr[i] == 0 :
                print(-1)
                return
            cnt += 1
            arr[i] //=  2
            
    print(cnt)
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()