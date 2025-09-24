
def main() :
    n = int(input())
    arr = []
    for _ in range(n) :
        a,b = list(map(int , input().split()))
        arr.append((a , b))
    
    def check(target) :
        cnt = 0
        for a , b in arr :
            if target - cnt - 1 <= a and cnt <= b :
                cnt += 1

        return cnt >= target
    
    l = 0
    r = n   
    ans = None
    while l <= r :
        mid = (l + r)//2
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    print(ans)

t = int(input())
for i in range(t) : main()