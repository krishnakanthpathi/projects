# String Matching

base = 5689
mod = int(1e9 + 7)

string = input()
pattern = input()

n = len(string)
m = len(pattern)

if m > n : 
    print(0)
    exit()

hashes = [0] * (n + 1)
basepow = [1] * (n + 1)

for i in range(1, n + 1):
    char = ord(string[i - 1]) - ord("a") + 1
    hashes[i] = (hashes[i - 1] * base + char) % mod
    basepow[i] = (basepow[i - 1] * base) % mod

res = 0
hashp = 0
for i in range(m):
    char = ord(pattern[i]) - ord("a") + 1
    hashp = (hashp * base + char) % mod

i = 0
for j in range(n) :
    if j - i + 1 > m :
        i += 1
    l = i + 1
    r = j + 1
    prefix = hashes[r]
    suffix = hashes[l - 1] * basepow[r - l + 1] % mod
    if (prefix - suffix + mod)%mod == hashp :
        res += 1

print(res)





