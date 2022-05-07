class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(index):
            if index == n:
                return 0
            start, end, tip = rides[index]
            ans = dp(index + 1)
            j = bisect_left(rides, [end, 0, 0])
            ans = max(ans, end - start + tip + dp(j))
            return ans
        
        n = len(rides)
        rides.sort()
        return dp(0)