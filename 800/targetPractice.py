t = int(input().strip())
for _ in range(t):
    grid = [input().strip() for _ in range(10)]
    n = 10
    res = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == "X" :
                X , Y = 1 + i%5 , 1 + j%5
                res += min(X , Y)
    print(res)
