n , m = map(int , input().split())

adj = {}
for _ in range(m) :
    s,d = map(int,input().split())
    if s not in adj :
        adj[s] = []
    if d not in adj :
        adj[d] = []
    adj[s].append(d)
    adj[d].append(s)

k = int(input())

office = set([i for i in range(n)])
home = set()
r = 0
roster = 0
while roster < k :
    for edge in adj :
        o_c = 0
        h_c = 0
        for nei in adj[edge] :
            if nei in office :
                o_c += 1
            else:
                h_c += 1
        if edge in office and (o_c > 3  or o_c < 3):
            office.remove(edge)
            home.add(edge)
        if edge in home and (h_c > 3 or h_c < 3) :
            office.add(edge)
            home.remove(edge)
    r += 1
    roster += len(office)

print(r)
