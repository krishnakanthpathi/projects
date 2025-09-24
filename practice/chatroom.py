string = input()

hello = "hello"
i = 0
for c in string:
    if c == hello[i]:
        i += 1
        if i == 5:
            print("YES")
            exit()
print("NO")
exit()