from bisect import bisect_left
from functools import lru_cache

def maxTaxiEarnings(n, rides):
    # @lru_cache(None)
    def dp(index, ans):
        if index == n:
            return 0
        start, end, tip = rides[index]
        # ans = dp(index + 1)
        j = bisect_left(rides, [end, 0, 0])
        # print("before: ", f"index : {index}", end, start, tip, j, ans)
        # if index == 3:
        #     import pdb; pdb.set_trace()
        value = dp(j, ans)
        print(f"index: {index} j: {j} dp(j): {value}")
        ans = max(ans, end - start + tip + value)
        # print("after: ", f"index : {index}", end, start, tip, j, ans)
        return ans
    
    n = len(rides)
    ans = 0
    rides.sort()
    return dp(0, ans)

n = 20
rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
maxTaxiEarnings(n, rides)