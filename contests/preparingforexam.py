def main():
    n, m, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    q = set(map(int, input().split()))  
    res = []
    known = set(q)
    for val in a:
        flag = False
        if val in known:
            flag = True
        known.add(val)
        res.append("1" if len(known) == n else "0")  
        if not flag:
            known.remove(val)

    print("".join(res))  

t = int(input())
for _ in range(t):
    main()
