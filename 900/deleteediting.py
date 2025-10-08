def main():
    s, t = input().split()
    visited = set()
    n , m = len(s) , len(t)
    i , j = n - 1 , m - 1
    while i >= 0 and j >= 0:
        if s[i] != t[j]:
            visited.add(s[i])
            i -= 1
        else:
            if s[i] in visited :
                print("NO")
                return
            i -= 1
            j -= 1
    print("YES" if j < 0 else "NO")
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()