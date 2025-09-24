MOD = int(1e9 + 7)

def add(x, y):
    return (((x % MOD) + (y % MOD)) % MOD + MOD) % MOD

def mul(x, y):
    return ((x % MOD) * (y % MOD)) % MOD

def binpow(x, y):
    z = 1
    while y:
        if y % 2 == 1:
            z = mul(z, x)
        x = mul(x, x)
        y //= 2  # Integer division
    return z

def inv(x):
    return binpow(x, MOD - 2)

def divide(x, y):
    return mul(x, inv(y))
