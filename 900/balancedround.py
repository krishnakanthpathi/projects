def main() :
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    l = res = 0
    for i in range(1 , n) :
        if arr[i] - arr[i - 1] > k :
            l = i
        res = max(res, i - l)
    print(n - res - 1)

if __name__ == "__main__" :
    t = int(input())
    for _ in range(t) :
        main()