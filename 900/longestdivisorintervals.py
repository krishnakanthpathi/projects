
def main():
    n = int(input())
    
    r = 1
    while n % r == 0 :
        r += 1
    
    print(r - 1)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()