import random
    
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 ]

cnt = 0
for prime in primes:
    print(prime)
    cur = input()
    if cur == "yes" :
        cnt += 1
for val in [4 , 9 , 25 , 49] :
    print(val)
    cur = input()
    if cur == "yes" :
        cnt += 1
if cnt <= 1 :
    print("prime")
else:
    print("composite")