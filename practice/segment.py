
def main() :
    n , k  = list(map(int , input().split()))
    w  = list(map(int , input().split()))
    c  = list(map(int , input().split()))
    res = 0
    cur_w = 0
    cur_c = 0
    l = 0
    for r in range(n) :
        cur_c += c[r]
        cur_w += w[r]
        while l <= r and cur_w > k :
            cur_w -= w[l]
            cur_c -= c[l]
            l += 1
        res = max(res , cur_c)

    print(res)
main()