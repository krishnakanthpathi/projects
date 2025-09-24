from collections import defaultdict

def longest_repeating_substring(string):
    n = len(string)
    
    # Two different primes for double hashing
    mod1 = 10**9 + 7
    mod2 = 10**9 + 9
    base = 5689  # Random prime base

    # Precompute hashes and powers
    hashes1 = [0] * (n + 1)
    hashes2 = [0] * (n + 1)
    powers1 = [1] * (n + 1)
    powers2 = [1] * (n + 1)

    for i in range(1, n + 1):
        hashes1[i] = (hashes1[i - 1] * base + ord(string[i - 1]) - ord("a") + 1) % mod1
        hashes2[i] = (hashes2[i - 1] * base + ord(string[i - 1]) - ord("a") + 1) % mod2
        powers1[i] = (powers1[i - 1] * base) % mod1
        powers2[i] = (powers2[i - 1] * base) % mod2

    res = ""
    left, right = 1, n

    # Binary search on length of repeating substring
    while left <= right:
        mid = (left + right) // 2
        seen_hashes = set()
        found_string = ""

        for j in range(n - mid + 1):
            l, r = j + 1, j + mid  # Convert to 1-based index
            
            # Compute double hash (hash1, hash2) to avoid collisions
            hash1 = (hashes1[r] - (hashes1[l - 1] * powers1[r - l + 1]) % mod1 + mod1) % mod1
            hash2 = (hashes2[r] - (hashes2[l - 1] * powers2[r - l + 1]) % mod2 + mod2) % mod2
            
            hash_pair = (hash1, hash2)

            if hash_pair in seen_hashes:
                found_string = string[j:j + mid]
                break
            seen_hashes.add(hash_pair)

        if found_string:
            res = found_string
            left = mid + 1
        else:
            right = mid - 1

    return res if res else -1

# Input and Output
string = input().strip()
print(longest_repeating_substring(string))
