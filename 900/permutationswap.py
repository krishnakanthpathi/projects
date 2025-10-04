import math

def main() :
    
    n = int(input())
    arr = list(map(int, input().split()))
    index_map = {v: i for i, v in enumerate(arr)}
    sorted_arr = sorted(arr)
    
    ans = None
    for i in range(n):
        cur = sorted_arr[i]
        j = index_map[cur]
        if ans is None :
            ans = abs(j - i)
        else :
            ans = math.gcd(ans, abs(j - i) )
    print(ans)
if __name__ == "__main__" :
    t = int(input())
    for _ in range(t) :
        main()