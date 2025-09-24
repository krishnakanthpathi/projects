t = int(input())

for _ in range(t) :
    n = input()
    total = 0
    for val in n  :
        total += int(val)

    if total % 9 == 0 or total%9 == 2 or total%9 == 3 :
        print("YES")
    else:
        print("NO")
