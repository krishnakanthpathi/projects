def main():
    n = int(input())
    def dfs(integer):
        if integer <= 3 :
            return 1
        return 2*dfs(integer//4)
    print(dfs(n))

t = int(input())
for _ in range(t):
    main()
