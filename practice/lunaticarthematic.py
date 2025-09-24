import math
def main() :
    n = int(input())
    arr = list(map(int , input().split()))
    gcds = []
    for idx in range(n // 2 + 1) :
        gcds.append(abs(arr[idx] - arr[n - idx - 1]))
    print(math.gcd(*gcds))

t = int(input())
for i in range(t) : main()