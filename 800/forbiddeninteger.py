
def main() :
    n , k , x = list(map(int , input().split()))
    if x != 1 :
        print("yes")
        print(n)
        print(*([1] * n))
        return 
    if  k >= 3 :
        print("YES")
        if n == 3 and k >= 3 :
            print(1)
            print(3)
        elif n%2 == 0 :
            print(n//2)
            print(*((n//2) * [2]))
        elif n%3 == 0 :
            print(n//3)
            print(*((n//3)*[3]))
        elif n%3 == 2 :
            no3 = n//3
            print(no3 + 1)
            print( no3 * "3 " + "2" )
        else:
            no3 = n//3
            print(no3 + 1)
            print( (no3 - 1) * "3 " + "2 2" )

    else:

        if n % 2 == 0 and k >= 2:
            print("YES")
            print(n//2)
            print(*(n//2 * [2]))
        else:
            print("NO")

t = int(input())
for i in range(t) : main()