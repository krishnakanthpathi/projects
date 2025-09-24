def count_good_substrings(s, good_chars, k):
    n = len(s)
    is_good = [c == '1' for c in good_chars]  # Boolean map for good characters
    
    # Prefix sum of bad characters
    bad_prefix = [0] * (n + 1)
    for i in range(n):
        bad_prefix[i + 1] = bad_prefix[i] + (0 if is_good[ord(s[i]) - ord('a')] else 1)
    
    # Hashing parameters (Three Bases & Moduli)
    P1, M1 = 31, 10**9 + 7
    P2, M2 = 37, 10**9 + 9
    P3, M3 = 41, 10**9 + 21
    
    power1 = [1] * (n + 1)  # Powers of P1
    power2 = [1] * (n + 1)  # Powers of P2
    power3 = [1] * (n + 1)  # Powers of P3
    hash_prefix1 = [0] * (n + 1)  # Hash prefix using P1
    hash_prefix2 = [0] * (n + 1)  # Hash prefix using P2
    hash_prefix3 = [0] * (n + 1)  # Hash prefix using P3

    # Compute power values and hash prefix for all bases
    for i in range(1, n + 1):
        power1[i] = (power1[i - 1] * P1) % M1
        power2[i] = (power2[i - 1] * P2) % M2
        power3[i] = (power3[i - 1] * P3) % M3
        hash_prefix1[i] = (hash_prefix1[i - 1] * P1 + (ord(s[i - 1]) - ord('a') + 1)) % M1
        hash_prefix2[i] = (hash_prefix2[i - 1] * P2 + (ord(s[i - 1]) - ord('a') + 1)) % M2
        hash_prefix3[i] = (hash_prefix3[i - 1] * P3 + (ord(s[i - 1]) - ord('a') + 1)) % M3

    substr_hashes = set()

    # Iterate over all substrings
    for i in range(n):
        for j in range(i, n):
            # Check if substring s[i...j] has at most k bad characters
            bad_count = bad_prefix[j + 1] - bad_prefix[i]
            if bad_count > k:
                break

            # Compute rolling hash for s[i...j] using all three bases
            hash_value1 = (hash_prefix1[j + 1] - hash_prefix1[i] * power1[j - i + 1]) % M1
            hash_value2 = (hash_prefix2[j + 1] - hash_prefix2[i] * power2[j - i + 1]) % M2
            hash_value3 = (hash_prefix3[j + 1] - hash_prefix3[i] * power3[j - i + 1]) % M3
            substr_hashes.add((hash_value1, hash_value2, hash_value3))  # Store as a tuple

    return len(substr_hashes)

# Reading input
s = input().strip()
good_chars = input().strip()
k = int(input().strip())

# Output result
print(count_good_substrings(s, good_chars, k))
