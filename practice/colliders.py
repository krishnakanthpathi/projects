import math
def primes(num):
    res = []
    for i in range(2 , int(math.sqrt(num)) + 1 ) :
        if num%i == 0 :
            res.append(i)
            while num%i == 0 : 
                num = num // i
    if num != 1 : 
        res.append(num)
    return res

def main() :
    n , m = list(map(int , input().split()))
    active = [ [0 , 0] for i in range(n + 1) ]
    group = [ 0 ] * ( n + 1 )
    for _ in range(m) :
        status , collider = list(map(str , input().split()))
        collider = int(collider)
        if status == "-" :
            if group[collider] == 0 : 
                print("Already off")
                continue
            check = True
            for i in primes(collider):
                if active[i][0] == 0 :
                    check = False
                    print("Already off")
                    break   
            if check:
                for i in primes(collider):
                    active[i][0] -= 1
                    active[i][1] = 0
                group[collider] = 0
                print("Success")
        else:
            check = True
            if group[collider] == 1 : 
                print("Already on")
                continue
            for i in primes(collider):
                if active[i][0] > 0 :
                    check = False
                    print(f"Conflict with {active[i][1]}")
                    break
            if check :
                group[collider] = 1
                for i in primes(collider):
                    active[i][0] += 1
                    active[i][1] = collider
                print("Success")


main()