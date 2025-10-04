def main():
    n = int(input())
    s = input().strip()
    greater = 0
    less = 0
    res = float('-inf')
    for i in range(n):
        if s[i] == '>' :
            greater += 1
        else :
            greater = 0
        if s[i] == '<' :
            less += 1
        else :
            less = 0
        res = max(res, greater, less)
        
    print(res + 1)

#    >. >  <   >  >  <.  >
# 100 99 98 100 99 98 100  99
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()