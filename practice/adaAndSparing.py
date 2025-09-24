import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    string = sys.stdin.readline().strip()

    base1 = 5689
    base2 = 31  # Different base for second hash
    mod1 = int(1e9 + 7)
    mod2 = int(1e9 + 9)

    hashs1 = [0] * (n + 1)
    hashs2 = [0] * (n + 1)
    basepow1 = [1] * (n + 1)
    basepow2 = [1] * (n + 1)

    # Compute hash values and power values
    for i in range(1, n + 1):
        char = ord(string[i - 1]) - ord("a") + 1
        hashs1[i] = (hashs1[i - 1] * base1 + char) % mod1
        hashs2[i] = (hashs2[i - 1] * base2 + char) % mod2
        basepow1[i] = (basepow1[i - 1] * base1) % mod1
        basepow2[i] = (basepow2[i - 1] * base2) % mod2

    hashset = set()
    i = 0

    # Sliding window
    for j in range(n):
        if j - i + 1 > k:
            i += 1
        if j - i + 1 != k:
            continue

        l = i + 1
        r = j + 1

        # Compute hash1
        prefix1 = hashs1[r]
        suffix1 = (hashs1[l - 1] * basepow1[r - l + 1]) % mod1
        cur1 = (prefix1 - suffix1 + mod1) % mod1

        # Compute hash2
        prefix2 = hashs2[r]
        suffix2 = (hashs2[l - 1] * basepow2[r - l + 1]) % mod2
        cur2 = (prefix2 - suffix2 + mod2) % mod2

        hashset.add((cur1, cur2))  # Store tuple of both hashes

    print(len(hashset))


t = int(sys.stdin.readline())
for _ in range(t):
    main()
