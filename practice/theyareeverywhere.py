
n = int(input())
s = input()
hashmap = {}
k = len(set(s))
l = 0
res = n
for r in range(n):
    hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
    while s[l] in hashmap and hashmap[s[l]] > 1:
        hashmap[s[l]] -= 1
        l += 1
    if len(hashmap) == k :
        res = min(res, r - l + 1)

print(res)


