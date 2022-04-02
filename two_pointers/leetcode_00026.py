class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        faster = 0
        slower = 0
        length = len(nums)
        while slower < length and faster < length:
            if nums[slower] == nums[faster]:
                faster += 1
            else:
                slower += 1
                nums[slower] = nums[faster]
        return slower + 1