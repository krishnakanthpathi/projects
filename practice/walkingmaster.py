import math

t = int(input())
for _ in range(t):
    sx , sy , x, y = map(int , input().split())
    
    if y < sy :
        print(-1)
    else:
        dx,dy = sx + ( y - sy ) , y
        if dx < x :
            print(-1)
        else:
            print( (dx - x) + ( y - sy ) )
    
# ____________|_______________
#      -2           2
#          .  -1    .