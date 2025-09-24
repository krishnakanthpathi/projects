from math import factorial

def ncr(n, m):
    if m > n:
        return 0
    return factorial(n) // (factorial(m) * factorial(n - m))

n = int(input())

N = n - 1
k = n
print((2 * ncr(N + k, N) - n) % 1000000007 )

