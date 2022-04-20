class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while (nums[right] - nums[left]) > mid:
                    left += 1
                count += right - left
            return count
        
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while (left < right):
            mid = (left + right) // 2
            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left