def lps(part: str) -> list[int]:
    i, length, m = 1, 0, len(part)
    lps = [0] * m

    while i < m:
        if part[i] == part[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps

def KMP(s: str, part: str, lps: list[int]) -> int:
    m, n = len(part), len(s)
    i = j = 0
    
    while i < n:
        if s[i] == part[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  
        elif j > 0:
            j = lps[j - 1]  
        else:
            i += 1 
    
    return -1  

