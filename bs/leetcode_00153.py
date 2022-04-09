class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                answer = min(answer, nums[left])
                left = mid + 1
            else:
                answer = min(answer, nums[mid])
                right = mid - 1
        return answer