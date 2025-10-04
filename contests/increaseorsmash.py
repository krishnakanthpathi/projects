
def main():
    n = int(input())
    arr = sorted(set(list(map(int, input().split()))))
    if n == 1 :
        print(0 if arr[0] == 0 else 1)
        return
    count = 0
    n = len(arr)
    for i in range(n - 1):
        count += arr[n - 1] - arr[i] 
    
    print(count + 1)
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()