import sys

def ask(left , right):
    print("?", right - left + 1 ,*([i  for i in range(left , right + 1)]))
    sys.stdout.flush()
    return int(input())

def tell(val):  
    print("!",val)

def checker(left , right , prefix):
    correct = ask(left , right)
    acutal = prefix[right] - prefix[left - 1]

    return acutal < correct
def main() :
    n =  int(input())
    arr = list(map(int , input().split()))
    prefix = [ 0 ]
    for val in arr :
        prefix.append(prefix[-1] + val)
    l = 1
    r = n
    ans = -1
    while l <= r :
        mid = (l + r)  // 2
        if checker(l , mid , prefix) :
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    tell(ans)

t = int(input())
for i in range(t) : main()


