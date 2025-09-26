
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if len(arr) == 1:
        print("YES")
        print(*arr)
        return
    if all(x == arr[0] for x in arr):
        print("NO")
        return
    else:
        print("YES")
        arr[1], arr[-1] = arr[-1], arr[1]
        print(*arr)
        return
if __name__ == "__main__":
    for _ in range(int(input())):
        main()





