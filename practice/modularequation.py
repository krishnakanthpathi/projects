import math
def factors(n , k) :
    fact = []
    for i in range(1 , math.floor(math.sqrt(n)) + 1) :
        if n % i == 0 :
            fact.append(i)
            if i*i != n  :
                fact.append(n // i)
    return [val  for val in fact if val > k ]

def main() :
    a , b = list(map(int , input().split()))
    if b > a : 
        print(0)
        return
    if a == b :
        print("infinity")
        return
    factor = factors(a - b , b)
    res = 0
    for val in factor :
        res += 1

    print(res)


main()