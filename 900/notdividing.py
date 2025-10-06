def main():
    n = int(input())
    arr = list(map(int ,input().split()))
    for i in range(n):
        arr[i] += 1
    for i in range(n) :
        
        if arr[i] % arr[i - 1] == 0 :
            arr[i] += 1
    print(*arr)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()