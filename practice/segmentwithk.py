
def main() :
    n , k = list(map(int , input().split()))
    nums = list(map(int , input().split()))
    hashmap = {}
    l = res = 0
    for r in range(n) :
        cur = nums[r]
        hashmap[cur] = 1 + hashmap.get(cur , 0)
        while len(hashmap) > k :
            res += r - l
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0 :
                del hashmap[nums[l]]
            l += 1
    while len(hashmap):
        res += r - l + 1
        hashmap[nums[l]] -= 1
        if hashmap[nums[l]] == 0 :
            del hashmap[nums[l]]
        l += 1
    print(res)
main()