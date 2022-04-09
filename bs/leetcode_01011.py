def cal_days(max_capacity, weights):
    capacity = 0
    num_days = 1
    for weight in weights:
        capacity += weight
        if capacity > max_capacity:
            capacity = weight
            num_days += 1
    return num_days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            num_days = cal_days(mid, weights)
            if num_days <= days:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans