def main():
    a , b , c = map(int, input().split())
    # a1 = a + b , a2 = a + 2b , a3 = a + 3b
    # 2a2 = a1 + a3

    answer = False
    new_a = 2 * b - c
    if new_a > 0 and new_a % a == 0 :
        answer = True
    new_b = (a + c) // 2
    if new_b > 0 and new_b % b == 0 and (c - a) % 2 == 0 :
        answer = True
    new_c = 2 * b - a
    if new_c > 0 and new_c % c == 0 :
        answer = True
    print("YES" if answer else "NO")
        
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main()    
    
    
    
