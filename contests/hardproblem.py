t = int(input())
for _ in range(t):
    m, a, b, c = map(int, input().split())
    res =  min(a , m) + min(b , m) 
    a = m - min(a , m)
    b = m - min(b , m)
    c = min(c , a + b)
    res += c
    print(res)
