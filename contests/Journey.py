
def main() :
    n ,a, b ,c = map(int , input().split())
    total = 3 * (n // (a + b + c))
    cnt = 0
    n = n % (a + b + c)
    while n > 0 :
        if cnt % 3 == 0 :
            n -= a
        elif cnt % 3 == 1 :
            n -= b
        else:
            n -= c
        total += 1
        cnt += 1
    print(total)


t = int(input())
for i in range(t) : main()