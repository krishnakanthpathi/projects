
class Solution:
    def frogJump(self, heights, k):
        n = len(heights)

        def dfs(i) :
            if i == n - 1:
                return 0
            if i >= n:
                return float('inf')
            ans = float('inf')
            for ik in range(1 , k + 1):
                if ik + i < n :
                    ans = min(
                        ans ,
                        dfs(ik + i) + abs( heights[i] - heights[ik + i])
                    )
            return ans

        # Memoization to avoid recomputation
        
                
        
    
# Example usage:
heights = [10, 30, 40, 20]
k = 2
solution = Solution()
print(solution.frogJump(heights, k))  # Output: 30 (minimum cost to reach the end)