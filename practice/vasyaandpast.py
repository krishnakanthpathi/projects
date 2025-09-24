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
    if n != 1 : pairs.append((n , 1))
    return pairs

import math
def main() :
    n = int(input())
    arr = set()
    for i in range(2 , n + 1):
        for temp in primefactors(i) :
            arr.add(temp)
    res = [ key**val for key , val in arr]
    print(len(res))
    print(*res)
main()