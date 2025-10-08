from collections import Counter


def main() :
    n = int(input())
    a = list(map(int, input().split()))
    hashmap = Counter(a)
    max_freq = max(hashmap.values())
    res = 0
    while max_freq < n :
        res += 1
        res += min(max_freq, n - max_freq)
        max_freq *= 2
    # 1  1  1 1 -- n
    # 3  6 12 24 -- n
    
    print(res)
    
if __name__ == "__main__" :
    t = int(input())
    for i in range(t) :
        main()