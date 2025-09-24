
def main() :
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split())) + [0]
    res = 0
    for i in range(n) :
        if a[i] >= b[i + 1] :
            res += (a[i] - b[i + 1])
    print(res)
    

t = int(input())
for i in range(t) : main()