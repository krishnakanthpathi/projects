import math

mod = 10**9 + 7
string = input()
hashmap = {}
for val in string :
    hashmap[val] = 1 + hashmap.get(val , 0)
res = math.factorial(len(string))
for key in hashmap : res = res//math.factorial(hashmap[key])
print(res%mod)