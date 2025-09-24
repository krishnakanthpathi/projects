t = int(input())  # Number of test cases

for _ in range(t):
    n, m = map(int, input().split())  # Lengths of x and s
    x = input().strip()
    s = input().strip()
    
    current_x = x
    operations = 0
    
    while len(current_x) <= 26*26:
        if s in current_x:  # Check if `s` is a substring
            print(operations)
            break
        current_x += current_x  
        operations += 1
    else:
        print(-1)  # If loop completes without finding `s`
