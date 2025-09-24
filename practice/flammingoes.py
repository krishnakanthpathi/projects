n = int(input())
res = [0]
for i in range(2,n+1):
    print("?",1,i)
    cur = int(input())
    res.append(cur)

print("?",2,n)
last = int(input())
frst = res[-1] - last
res[0] = frst
ans = [ frst ]
for i in range(1 , n):
    ans.append(res[i] - res[i - 1])

print("!" , *ans)