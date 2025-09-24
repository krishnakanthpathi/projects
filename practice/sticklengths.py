n = int(input())    
sticks = list(map(int, input().split()))
sticks.sort()
avg = sticks[n // 2]
res = 0
for i in range(n):
    res += abs(sticks[i] - avg)
print(res)



