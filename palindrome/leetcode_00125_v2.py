"""
@author: Coder The Grey
@date  : 2022-05-22
@leetcode: https://bit.ly/3lvWJbN
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                clean_str += char.lower()

        center = (0 + len(clean_str) - 1) // 2
        left = center
        right = center
        if len(clean_str) % 2 == 0:
            right = center + 1
        while left >= 0 and right < len(clean_str) and clean_str[left] == clean_str[right]:
            left -= 1
            right += 1

        if (right - left - 1) == len(clean_str):
            return True
        return False
