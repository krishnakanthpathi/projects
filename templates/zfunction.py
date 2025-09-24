
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]

    return z


class Solution:
    def beautifulSplits(self, nums):
        n = len(nums)
        lps1 = self.z_function(nums)
        count = 0

        for i in range(1, n - 1):
            m = n - i
            temp = nums[i:]
            lps2 = self.z_function(temp)

            for j in range(1, m):
                if (j >= i and lps1[i] >= i) or (lps2[j] >= j):
                    count += 1

        return count

