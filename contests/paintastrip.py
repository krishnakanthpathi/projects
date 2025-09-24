t = int(input())

for _ in range(t) :
    n  = int(input())
    cur = 9
    itr = 2
    if n == 1 :
        print(1) 
    else:
        while True :
            if n <= cur :
                print(itr)
                break
            itr += 1           
            cur = cur*2 + 1
            
    
