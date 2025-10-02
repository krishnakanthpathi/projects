t = int(input())

def sumofAP(a , d , n):
    return (n/2) * (2*a + (n-1)*d)

for _ in range(t):
    n ,k , x= map(int, input().split())
    # print(n , k , x)
    # print(sumofAP(1 , 1 , k) , sumofAP(n-k+1 , 1, k))
    if(sumofAP(1 , 1 , k) <= x and x <= sumofAP(n-k+1 , 1, k)):
        print("YES")
    else:
        print("NO")