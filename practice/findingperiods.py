string = input()

n = len(string)
mod = 10**9 + 7
hashes = [0] * (n + 1)
powers = [1] * (n + 1)
base = 5689

for i in range(1, n + 1):
    hashes[i] = (hashes[i - 1] * base + ord(string[i - 1] ) - ord("a") + 1 ) % mod
    powers[i] = (powers[i - 1] * base) % mod
    
for i in range(1, n + 1):
    j = 0
    flag = False
    frst = hashes[i]
    while j + i < n:
        l = j + 1
        r = j + i 
        prefix = hashes[r]
        suffix = (hashes[l - 1] * powers[r - l + 1]) % mod
        # print(string[l-1:r] ,frst , (prefix - suffix + mod)%mod)
        if (prefix - suffix + mod)%mod != frst:
            flag = True
            break
        j += i
    if not flag:
        extra = n - j 
        l = j + 1
        r = j + extra
        prefix = hashes[r]
        suffix = (hashes[l - 1] * powers[r - l + 1]) % mod
        last = (prefix - suffix + mod) % mod
        frst = hashes[extra]
        # print(extra , frst , last)
        if(frst==last): print(i , end=" ")
         