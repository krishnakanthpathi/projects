import sys
n , t = list(map(int , input().split()))
k =  int(input())

def ask(left , right):
    print("?",left , right)
    # sys.stdout.flush()
    total = int(input())
    zeros = (right - left + 1) - total
    return zeros >= k

def tell(val):  
    print("!",val)


l = 1 
r = n
ans = -1

while l <= r :
    mid = (l + r)//2

    if ask(1 , mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

    
tell(ans)




