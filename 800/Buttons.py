t = int(input())
for _ in range(t) :
    a,b,c = map(int,input().split())
    if c%2 :
        a += 1
    a += c // 2
    b += c
    if a > b :
        print("First")
    else:
        print("Second") 