t = int(input().strip())
for _ in range(t):
    grid = [input().strip() for _ in range(10)]
    n = 10
    res = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == "X" :
                if i <= 5 :
                    X =  5 if i == 5 else (1 + i%5) 
                if j <= 5 :
                    Y = 5 if j == 5 else (1 + j%5)
                if i > 5 :
                    X = 1 + (10 - i - 1)%5
                if j > 5 :
                    Y = 1 + (10 - j - 1)%5

                res += min(X , Y)
        print()
                
    print(res)