t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    rem = n%k
    if rem%2 == 0 :
        print("YES")
    else:
        print("NO")