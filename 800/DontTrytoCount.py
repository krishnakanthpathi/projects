t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    source = input()
    dest = input()
    ans = -1
    for idx , val in enumerate(source):
        j = idx
        i = 0
        while i < m and source[j] == dest[i] :
            i += 1
            j = (j + 1)%n
        if i == m :
            ans = 0 if i <= j else i - j
            break
    print(ans)

