import math
def primefactors(n):
    pairs = []
    for i in range(2 , int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            count = 0
            while n % i == 0 :
                n = n // i
                count += 1
            pairs.append((i , count))
    return pairs
def main() :
    n = int(input())
    arr = list(map(int , input().split()))
    res = 0
    pairs = []
    for i in arr :
        primes = primefactors(i)

    

t = int(input())
for i in range(t) : main()