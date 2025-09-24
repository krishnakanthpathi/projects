def main() :
    n , k  = list(map(int , input().split()))
    string = input()

    res = 0
    acnt = 0
    bcnt = 0
    cur = 0
    l = 0
    for r in range(n) :
        acnt += 1 if string[r] == "a" else 0
        bcnt += 1 if string[r] == "b" else 0
        if string[r] == "b" : cur += acnt
        while cur > k  :
            acnt -= 1 if string[l] == "a" else 0
            bcnt -= 1 if string[l] == "b" else 0
            if string[l] == "a" : cur -= bcnt
            l += 1
        res = max(res , r - l + 1)

    print(res)
main()