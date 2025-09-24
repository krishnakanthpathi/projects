base = 5689
mod = int(1e9 + 7)

string = "hello"
n = len(string)

hashes = [0] * (n + 1)
basepow = [1] * (n + 1)

for i in range(1, n + 1):
    char = ord(string[i - 1]) - ord("a") + 1
    hashes[i] = (hashes[i - 1] * base + char) % mod
    basepow[i] = (basepow[i - 1] * base) % mod

print(hashes[n])
l , r = 0 , n - 1

l += 1 
r += 1
prefix = hashes[r]
suffix = hashes[l - 1] * basepow[r - l + 1] % mod
print((prefix - suffix + mod) % mod)    





