def count_prefixes():
    n , m = map(int,input().split())
    
    strings = [input().strip() for _ in range(n)]
    
    prefix_freq = {}
    total_elements = {}

    for string in strings:
        for i in range(len(string)):
            prefix = string[:i+1]
            length = len(prefix)
            if length not in prefix_freq:
                prefix_freq[length] = {}
                total_elements[length] = 0
            if prefix in prefix_freq[length]:
                prefix_freq[length][prefix] += 1
            else:
                prefix_freq[length][prefix] = 1
            total_elements[length] += 1
    res = 0
    for string in strings:
        for i in range(len(string) - 1):
            prefix = string[:i+1]
            length = len(prefix)
            res = res + (total_elements[length] - prefix_freq[length][prefix])
            
    print(res)
count_prefixes()