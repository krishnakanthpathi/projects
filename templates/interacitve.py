import sys
import math
from collections import *

def ask(left , right):
    print("?", *([i + 1 for i in range(left , right + 1)]))
    sys.stdout.flush()
    # total = 

def tell(val):  
    print("!",val)
    

def main() :
    n =  int(input())
    arr = list(map(int , input().split()))


t = int(input())
for i in range(t) : main()