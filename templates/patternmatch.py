def RollingHash(self, pattern , word) :
        m = len(pattern)
        mod = int(1e9 + 7)
        n = len(word)
        if m > n : return False
        base = 29
        pattern_hash = 0
        for char in pattern : 
            ordinal = ord(char) - ord("a") + 1
            pattern_hash = (
                pattern_hash * base + ordinal
            ) % mod
        
        l = 0
        cur_hash = 0
        for r in range(n) :
            ordinal = ord(word[r]) - ord("a") + 1
            cur_hash = (
                cur_hash * base + ordinal
            )%mod
            if r - l + 1 > m :
                ordinal = ord(word[l]) - ord("a") + 1
                power = r - l
                cur_hash = (cur_hash - (ordinal * (base**(power))))%mod
                l += 1
            if cur_hash == pattern_hash :
                return True
        return False


