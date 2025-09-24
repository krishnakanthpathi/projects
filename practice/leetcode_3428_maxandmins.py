def mod_pow(base, exp, mod):
    result = 1
    while exp:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact[n] = mod_pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    return fact, inv_fact

def nCr(n, r, fact, inv_fact, mod):
    if n == 0 and r == 0 :
        return 0
    if r > n or r < 0 :
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        mod = int(1e9 + 7)
        n = len(nums)
        fact, inv_fact = factorials(n + 1 , mod)
        res = 0
        prev = 0
        for i in range(n) :
            if i > 0 and nums[i] == nums[i - 1]:
                prev += 1
            else:
                prev = 0
                
            picks = n - i - 1 + prev
            includes = (nCr(picks , k - 1 , fact , inv_fact , mod) if k - 1 > 0  else 0) + 1
            res = (res + nums[i] * includes ) % mod
            print(nums[i], picks, includes)
            
        prev = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] == nums[i + 1]:
                prev += 1
            else:
                prev = 0
            picks = i + prev
            includes = (nCr(picks , k - 1 , fact , inv_fact , mod) if k - 1 > 0  else 0) + 1
            res = (res + nums[i] * includes) % mod
            print(nums[i], picks, includes)
        return res % mod