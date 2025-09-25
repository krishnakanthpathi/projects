import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for val in a :
        res ^= val
    if n % 2 == 0 and res != 0 :
        res = -1
    sys.stdout.write(str(res) + "\n")
    sys.stdout.flush()
