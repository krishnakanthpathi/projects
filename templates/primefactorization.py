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
# prime factorization by sieve

