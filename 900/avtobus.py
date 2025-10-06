def main() :
    n = int(input())
    if n % 2 == 0 and n >= 4:
        maxi = n//4 
        mini = n//6 if n%6 == 0 else n//6 + 1
        print(mini , maxi)
        return (maxi , mini)
    print(-1)
    return -1
    
if __name__ == "__main__" :
    t = int(input())
    for i in range(t) :
        main()