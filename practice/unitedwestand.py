t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    min_element = min(arr)
    min_array = [x for x in arr if x == min_element]
    remaining_array = [x for x in arr if x != min_element]
    if remaining_array:
        print(len(min_array), len(remaining_array))
        print(" ".join(map(str, min_array)))
        print(" ".join(map(str, remaining_array)))
    else:
        print(-1)
