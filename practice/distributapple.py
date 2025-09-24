from math import factorial

def ncr(n, m):
    if m > n:
        return 0
    return factorial(n) // (factorial(m) * factorial(n - m))

n , m = map(int, input().split())

print(
    ncr(n + m - 1 , n - 1)% 1000000007
)

