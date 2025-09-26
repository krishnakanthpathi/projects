t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 1
    res = -1
    for val in a:
        total *= val
    left = 1
    cnt = 0
    for val in a :
        cnt += 1
        left = (left * val)
        total //= val
        if left == total:
            res = cnt
            break
    print(res)