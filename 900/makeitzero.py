
def xor_of_list(arr ):
    result = 0
    for num in arr:
        result ^= num
    return result

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # print(xor_of_list(arr[:n-1]) , xor_of_list(arr[n - 1:]))
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n - 1)
        print(1, n - 1)
        print(n - 1 , n)
        print(1 , n)

        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()