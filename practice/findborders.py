
s = input()
n = len(s)

mod = int(1e9 + 7)
hashs = [0] * (n + 1)
basepow = [1] * (n + 1)
base = 5689

for i in range(1 , n + 1) :
    char = ord(s[i - 1]) - ord("a") + 1
    hashs[i] = (hashs[i - 1] * base + char) %mod
    basepow[i] = (basepow[i - 1] * base) % mod
res = []
for length in range(1 , n) :
    prefix = hashs[length]
    suffix = (hashs[n] - hashs[n - length] * basepow[length] + mod) % mod
    if(prefix == suffix): res.append(length)
print(*res)