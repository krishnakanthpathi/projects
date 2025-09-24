
n = int(input())
arr = list(map(int  , input().split()))
print(min(
    [ abs(val) for val in arr]
))
