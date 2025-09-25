import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    l , r = 0, n-1
    while l < r and ( (a[l] == "0" and a[r] == "1") or (a[l] == "1" and a[r] == "0") ) :
        l += 1
        r -= 1
    sys.stdout.write(str(r- l + 1) + "\n")
    sys.stdout.flush()
