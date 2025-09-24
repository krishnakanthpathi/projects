t = int(input())
for _ in range(t):
    a = input()
    res = ""
    for char in a[::-1] :
        if char == "q" :
            res += "p"
        elif char == "p" :
            res += "q"
        else:
            res += "w"
    print(res)