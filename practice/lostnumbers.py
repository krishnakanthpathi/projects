import sys
import math
from collections import *

def ask(left , right):
    print("?", left , right)
    sys.stdout.flush()
    return int(input())

def tell(val):  
    print("!",*val)
    

def main() :
    hashmap = {}
    arr = [ 4 , 8, 15, 16, 23, 42 ]
    #       1   2   3   4   5  6       
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
            hashmap[arr[i] * arr[j]] = [arr[i] ,  arr[j]]
    ask1 = ask(1 , 3)
    ask2 = ask(3 , 5)
    ask3 = ask(2, 4)
    ask4 = ask(4 , 6)
    frst , sec = hashmap[ ask1 ] , hashmap[ ask2 ]
    thrd , fourth = hashmap[ ask3 ] , hashmap[ ask4 ] 

    res = [0]*6
    x1 , x2 = frst 
    y1 , y2 = sec
    if x1 in frst and x1 in sec :
        res[2] = x1
        res[0] = ask1//x1
        res[4] = ask2//x1
    else:
        res[2] = x2
        res[0] = ask1//x2
        res[4] = ask2//x2

    x1 , x2 = thrd 
    y1 , y2 = fourth
    if x1 in thrd and x1 in fourth :
        res[3] = x1
        res[1] = ask3//x1
        res[5] = ask4//x1
    else:
        res[3] = x2
        res[1] = ask3//x2
        res[5] = ask4//x2

    
    tell(res)
main()