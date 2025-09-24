import math
def main() :
    n , m = list(map(int , input().split()))
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    cur = 0
    for i in range(1 , n):
        cur = math.gcd(cur , a[i] - a[i - 1])
    res = []
    for i in range(m) :       
        res.append(math.gcd(cur , a[0] + b[i]))
    print(*res)
    
"""
gcd inutition
1 25 121 169
1 2 7 23 
gcd( 1 + 1 , 1 + 2 , 1 + 7 , 1 + 23 )
gcd(a , b) -> gcd(a , a - b)
gcd(a1 + b1 , a1 + b2 ) -> gcd(a1 + b1 , a1 - a1 - b1 + b2)
gcd(a1 + b1 , -b1 + b2 ) # a1 + b3
gcd(a1 + b1 , -b1 + b3 ) -b1 + b3 +b1 - b2 --> b3 - b2
gcd(a1 + b1 , -b1 + bn )                       bn - bn-1

gcd(a,b2 - b1 , b3 - b2 , b4 - b3 ........ bn - bn-1 )  

gcd(a1 + b1 , a2 + b1 , ... an + b1)
gcd(a1 + b1 , a2 - a1 , .. ,an - an-1)

"""
main()