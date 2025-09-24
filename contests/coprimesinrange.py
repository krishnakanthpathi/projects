
import math
def main() :
    arr = list(map(int , input().split()))
    print(arr[-1] - arr[0])

t = int(input())
for i in range(t) : main()