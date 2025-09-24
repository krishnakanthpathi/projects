string = input()

n = len(string)
mod = 10**9 + 7
base = 5689

hashes = [0] * (n + 1)
powers = [1] * (n + 1)

for i in range(1, n + 1):
    hashes[i] = (hashes[i - 1] * base + ord(string[i - 1]) - ord("a") + 1) % mod
    powers[i] = (powers[i - 1] * base) % mod

lens = []
for i in range(1, n):
    prefix = hashes[i] % mod
    suffix = (hashes[n] - (hashes[n - i] * powers[i]) % mod) % mod
    if prefix == suffix:
        lens.append(i)
        
res = ""
left = 0
right = len(lens) - 1
while left <= right:
    mid = (left + right) // 2
    i = lens[mid]
    
    j = 1
    frst = hashes[i]
    cnt = 0
 
    while j + i < n:
        l, r = j + 1, j + i
        prefix = hashes[r]
        suffix = (hashes[l - 1] * powers[r - l + 1]) % mod
 
        if (prefix - suffix + mod) % mod == frst:
            cnt += 2
            break
        j += 1 
 
    prefix = hashes[i] % mod
    suffix = (hashes[n] - (hashes[n - i] * powers[i]) % mod) % mod
 
 
    if prefix == suffix and cnt >= 1:
        res = string[:i]
        left = mid + 1
    else:
        right = mid - 1
    

print(res if res else "Just a legend")
