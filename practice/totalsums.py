
def main() :
    n , k  = list(map(int , input().split()))
    arr  = list(map(int , input().split()))
    cur = res = l = 0
    for r in  range(n) :
        cur += arr[r]
        while l <= r and cur > k :
            cur -= arr[l]
            l += 1
        print(r - l + 1 , cur)
        res += r - l + 1
        

    print(res)

main()