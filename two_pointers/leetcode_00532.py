class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        length = len(nums)
        slower = 0
        faster = 0
        counter = 0
        while faster < length and slower < length:
            if ((faster == slower) or (sorted_nums[faster] - sorted_nums[slower] < k)):
                faster += 1
            elif (sorted_nums[faster] - sorted_nums[slower] > k):
                slower += 1
            else:
                slower += 1
                counter += 1
                while (slower < length and (sorted_nums[slower] == sorted_nums[slower - 1])):
                    slower += 1
        return counter
