#User function Template for python3
from functools import cache
class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[0] * 3 for _ in range(n)]
        dp[0] = arr[0]
        
        for i in range(1 , n) :
            for j in range(3) :
                pick = arr[i][j]
                for k in range(3) :
                    if j != k :
                        dp[i][j] = max(
                            dp[i][j] , 
                            dp[i - 1][k] + pick
                        )

        return max(dp[-1])
    
    
#User function Template for python3
from functools import cache
class Solution:
    def maximumPoints(self, arr):
        n = len(arr)
        @cache
        def dfs(i , prev) :
            if i == n :
                return 0 
            ans = 0
            for j in range(3):
                pick = arr[i][j]
                if j != prev :
                    ans = max(ans , pick + dfs(i + 1 , j))
                    
            return ans
        return dfs(0 , -1)