t = int(input())

for _ in range(t) :
    n = int(input())
    a = 3
    cnt = 0
    while True :
        sqa = a*a
        b = ( sqa - 1 )// 2
        c = b + 1
        if c > n :
            break
        cnt += 1
        
        a += 2

    print(cnt)


    # a^2 = 2b + 1 right 
    # b = a2 - 1 // 2
    # b = c - 1


