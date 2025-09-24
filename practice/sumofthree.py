

def main() :
    n , k = list(map(int , input().split()))
    nums = list(map(int , input().split()))
    nums = [(nums[i] , i) for i in range(n)]
    nums.sort()

    for i, a in enumerate(nums):
        cur = k - a[0]
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum =  nums[l][0] + nums[r][0]
            if threeSum > cur:
                r -= 1
            elif threeSum < cur:
                l += 1
            else:
                print(*[ a[1] + 1 , nums[l][1] + 1, nums[r][1] + 1])
                return
                    
    print('IMPOSSIBLE')

main()