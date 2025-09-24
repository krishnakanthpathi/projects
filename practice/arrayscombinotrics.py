import math

n = int(input())
N = int(1e1 + 1)

arr = [0] * N
arr[0] = 1
for i in range(1 , N):
    arr[i] += i * arr[i - 1] * math.factorial(i)

print(2*arr[n] - n)
