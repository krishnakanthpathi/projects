def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_value = -1
    total_sum = 0
    
    for x in a:
        total_sum += x
        max_value = max(max_value, x)
    
    print(max(max_value * 2, total_sum))

solve()
