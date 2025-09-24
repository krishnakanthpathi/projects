import math
def main() :
    n = int(input())
    frst = 0
    sec = 0
    fc = sc = 0
    for i in range(n , 0 , -1) :
        cur = 2 ** i 
        frst_min = abs(frst + cur - sec)
        sec_min = abs(frst - (sec + cur))

        if sc == n // 2 or frst_min <= sec_min :
            frst += cur
            fc += 1
        else:
            sec += cur
            sc += 1

    print(abs(frst - sec))

t = int(input())
for i in range(t) : main()

#  2 4 8 16

# 16 2    8 4