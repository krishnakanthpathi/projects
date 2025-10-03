
def main() :
    a , b , n = map(int , input().split())
    arr = list(map(int , input().split()))
    ans = 0
    lessthan = b 
    for i in range(n) :
        if arr[i] >= a :
            ans += 1
        else:
            lessthan += arr[i] 
            
        
    print(ans * (a - 1) + lessthan )
        
    
    
if __name__ == "__main__" :
    t = int(input())
    for _ in range(t) :
        main()