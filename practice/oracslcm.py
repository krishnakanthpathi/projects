import math
from collections import defaultdict
def primefactors(num):
    primes = defaultdict(int)
    for i in range(2 , int(math.sqrt(num) + 1)):
        if num % i == 0 :
            cnt = 0
            while num%i == 0 :
                cnt += 1
                num //= i
            primes[i] += cnt
    if num != 1 : primes[num] = 1
    return primes
def inf():
    return float("inf") 
def main() :
    n = int(input())
    arr = list(map(int , input().split()))
    minimalprimes = defaultdict(inf)
    for val in arr :
        print(primefactors(val).items())
        for key , val in primefactors(val).items() :
            minimalprimes[key] = min(minimalprimes[key] , val)
    print(minimalprimes)

main()