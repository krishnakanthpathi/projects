
def main():
    x , n  = map(int, input().split())
    # x , x - 1 , x + 2 , x + 3 , x - 4 , x - 5 , x + 6 , x + 7 , x - 8 , x - 9 , x + 10 + 11
    # 0.    1       1.     0.      0        1.    1         0.      0.     1       1
    #. 0.   1.                -1                 1              -1               1
    #  10. 10
    #    10. 9   11.  14.  10. 5. 11. 18  10. 1
    #    1.  2.  3.   4.   5.  6. 7.  8.  9. 10
    # x , x + 1 , x - 2 , x - 3 , x + 4.    x + 5
    #  1.    0       0.     1.      1.  ,     0
    # 0.     -1.               1               -1
    # print(x , n)
    # -13 -12 -11 -10 -13 -8 -7 -6 -13 -4   -3  -2  -13  0 
    #    1.  2.  3.  4.  5. 6. 7.  8.  9. 10. 11. 12.   13
    shift = 0
    if n % 4 == 1 :
        shift = (n // 4) * 4 + 1
        if x % 2 == 0 :
            print(x - shift)
        else:
            print(x + shift)
        
    elif n % 4 == 2 :
        shift = 1
        if x % 2 == 0 :
            print(x + shift)
        else:
            print(x - shift)
    elif n % 4 == 3 :
        shift = n + 1
        if x % 2 == 0 :
            print(x + shift)
        else:
            print(x - n - 1 )
    else:
        print(x)
    
    

        
        
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()