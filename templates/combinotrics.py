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
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

def nPr(n, r, fact, mod):
    if r > n or r < 0:
        return 0
    return fact[n] * mod_pow(fact[n - r], mod - 2, mod) % mod
